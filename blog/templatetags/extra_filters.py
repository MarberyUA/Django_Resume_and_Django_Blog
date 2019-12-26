from django import template
from blog.models import Post

register = template.Library()

@register.filter()
def check(slug, name):
    post = Post.objects.get(slug=slug)
    try:
        post.likes.get(user_name=name)
        var = 'Unlike'
    except:
        var = 'Like'

    return var