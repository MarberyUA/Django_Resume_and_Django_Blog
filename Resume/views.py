from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.urls import reverse_lazy
from django.views import View
from django.core.files import File
from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.mail import send_mail
from .models import Post, ImageTag, GitHubProfile, Email
from .utils import *
from .forms import *
from .parser import github_parse
from Resume.models import gen_slug
from Resume_Engine.settings import DEFAULT_FROM_EMAIL
from django.template.loader import render_to_string
from django.contrib.auth.mixins import LoginRequiredMixin
from Resume_Engine.settings import STATICFILES_DIRS


# Create your views here.

class GitHubSettingsUpdate(LoginRequiredMixin, UpdateView):
    try:
        model = GitHubProfile
        form_class = GitHubUpdateForm
        success_url = reverse_lazy('about_me_url')
        raise_exception = True
    except:
        print('GitHub profile was not matched!')


class EmailSettingsUpdate(LoginRequiredMixin, UpdateView):
    try:
        model = Email
        form_class = EmailUpdateForm
        success_url = reverse_lazy('about_me_url')
        raise_exception = True
    except:
        print('email was not created!')


def projects_list(request):
    projects = Post.objects.all()
    email = Email.objects.get(slug='email')
    github = GitHubProfile.objects.get(slug='github')
    return render(request, 'resume/index.html', context={'posts': projects, 'github': github, 'email': email})


def tag_list(request):
    tags = ImageTag.objects.all()
    return render(request, 'resume/tags_list.html', context={'tags': tags})


def contact(request):
    if request.method == 'GET':
        forms = ContactForm()
        return render(request, 'base.html', context={'forms': forms})
    else:
        send_mail(request.POST.get('subject', None), request.POST.get('message', None), DEFAULT_FROM_EMAIL, [request.user.email], fail_silently=False)
        # except AttributeError:
        #     output_info = 'You did not log in to send the message'
        #     return render(request, 'base.html', context={'message': output_info})
        return render(request, 'base.html')


class AddImage(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = AddImageForm
    template_name = 'resume/add_project_image.html'
    raise_exception = True


class PinPost(LoginRequiredMixin, View):

    def post(self, request, slug):
        post_pin = Post.objects.get(slug=slug)
        if post_pin.pin:
            post_pin.pin = False
            post_pin.save()
        else:
            post_pin.pin = True
            post_pin.save()
        return render(request, 'resume/pin_post.html', context={'pinned_post': post_pin})

    raise_exception = True


class AddTechnology(LoginRequiredMixin, View):
    def get(self, request, slug):
        obj = Post.objects.get(slug=slug)
        form = AddTechnologyForm()
        return render(request, 'resume/add_technologists.html', context={'form': form, 'post': obj})

    def post(self, request, slug):
        obj = Post.objects.get(slug=slug)
        form = AddTechnologyForm(request.POST, request.FILES)
        if form.is_valid():
            tag = form.save()
            obj.technologists.add(tag)
            obj.save()
            return redirect(obj)
        return render(request, 'resume/add_technologists.html', context={'form': form, 'post': obj})

    raise_exception = True


class LoadProjects(LoginRequiredMixin, View):
    def post(self, request):
        for post in Post.objects.all():
            if not post.pin:
                post.delete()
        link = GitHubProfile.objects.get(id=1)
        github_projects = github_parse(link.link)
        for object in github_projects:
            Post.objects.create(title=object['title'], slug=gen_slug(object['title']), description=object['description'],
                                programme_language=object['programm_language'], update_time=object['update_time'],
                                link=object['link'])
        new_projects = Post.objects.all()
        return render(request, 'resume/load_projects.html', context={'posts': new_projects})

    raise_exception = True


class ProjectDetail(ObjectDetailMixin, View):
    model = Post
    template = 'resume/project_detail.html'


class ProjectCreate(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'resume/project_create.html'
    raise_exception = True


class ProjectEdit(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'resume/project_edit.html'
    raise_exception = True


class ProjectDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'resume/project_delete.html'
    success_url = reverse_lazy('about_me_url')
    raise_exception = True


class ImageTagDetail(ObjectDetailMixin, View):
    model = ImageTag
    template = 'resume/tag_detail.html'


class ImageTagCreate(LoginRequiredMixin, CreateView):
    model = ImageTag
    form_class = ImageTagForm
    template_name = 'resume/tag_create.html'
    raise_exception = True


class ImageTagDelete(LoginRequiredMixin, DeleteView):
    model = ImageTag
    template_name = 'resume/tag_delete.html'
    success_url = reverse_lazy('tag_list_url')
    raise_exception = True
