from django.shortcuts import render, redirect, HttpResponse
from blog.utils import *
from django.views import View

from blog.models import Post, Tag, LikeAction
from blog.forms import TagForm, PostForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from django.db.models import Q


# Create your views here.
def posts_list(request):
    search_quary = request.GET.get('search', '')

    if search_quary:
        posts = Post.objects.filter(Q(title__icontains=search_quary) | Q(body__icontains=search_quary))
    else:
        posts = Post.objects.all()

    paginator = Paginator(posts, 2)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        previous_url = '?page={0}'.format(page.previous_page_number())
    else:
        previous_url = ''

    if page.has_next():
        next_url = '?page={0}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': previous_url
    }

    return render(request, 'blog/index.html', context=context)


class PressLike(View):
    def post(self, request, slug):
        post = Post.objects.get(slug=slug)
        name = request.user.username
        test_action = LikeAction(user_name=name)

        for object in post.likes.all():
            if test_action.user_name == object.user_name:
                object.delete()
                object.save()
                test_action = 'tested'
        if test_action != 'tested':
            action = LikeAction(user_name=name, press_like=True)
            action.save()
            post.likes.add(action)
            post.save()
            return redirect('posts_list_url')
        else:
            render(request, 'blog/includes/post_card_template.html')
        return redirect('posts_list_url')




def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = PostForm
    template = 'blog/post_create_form.html'
    raise_exception = True


class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Post
    form_model = PostForm
    template = 'blog/post_update_form.html'
    raise_exception = True


class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete_form.html'
    redirect_link = 'posts_list_url'
    raise_exception = True


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = TagForm
    template = 'blog/tag_create.html'
    raise_exception = True


class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Tag
    form_model = TagForm
    template = 'blog/tag_update_form.html'
    raise_exception = True


class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Tag
    template = 'blog/tag_delete_form.html'
    redirect_link = 'tag_list_url'
    raise_exception = True
