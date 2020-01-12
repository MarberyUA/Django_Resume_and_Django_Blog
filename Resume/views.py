from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.mail import send_mail
from .models import Post, ImageTag
from .utils import *
from .forms import *
from .parser import github_parse
from Resume_Engine.settings import DEFAULT_FROM_EMAIL
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


class ProjectsList(View):
    def get(self, request):
        projects = Post.objects.all()
        form = ContactForm()
        return render(request, 'resume/index.html', context={'posts': projects, 'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        error = ''
        if form.is_valid():
            send_mail(form.cleaned_data['subject'], form.cleaned_data['message'], DEFAULT_FROM_EMAIL, ['marberymain@gmail.com'], fail_silently=False)

        return redirect('about_me_url')


def tag_list(request):
    tags = ImageTag.objects.all()
    return render(request, 'resume/tags_list.html', context={'tags': tags})


class Contact(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'resume/send_mail_form.html', context={'forms': form})



class AddImage(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = AddImageForm
    template_name = 'resume/add_project_image.html'
    raise_exception = True


class PinPost(LoginRequiredMixin, View):

    def post(self, request, id):
        post_pin = Post.objects.get(id=id)
        if post_pin.pin:
            post_pin.pin = False
            post_pin.save()
        else:
            post_pin.pin = True
            post_pin.save()
        return render(request, 'resume/pin_post.html', context={'pinned_post': post_pin})

    raise_exception = True


class AddTechnology(LoginRequiredMixin, View):
    def get(self, request, id):
        obj = Post.objects.get(id=id)
        form = AddTechnologyForm()
        return render(request, 'resume/add_technologists.html', context={'form': form, 'post': obj})

    def post(self, request, id):
        obj = Post.objects.get(id=id)
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
        link = 'https://github.com/MarberyUA?tab=repositories'
        github_projects = github_parse(link)
        for object in github_projects:
            Post.objects.create(title=object['title'], description=object['description'],
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
