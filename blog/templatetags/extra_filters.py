from django import template
from blog.models import LikeAction

register = template.Library()

@register.filter()
def is_user_liked(post_id, user_id):
    try:
        is_liked = LikeAction.objects.get(post_id=post_id, user_id=user_id)
        return True
    except:
        return False