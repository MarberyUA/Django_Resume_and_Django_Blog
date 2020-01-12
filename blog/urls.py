from django.urls import path
from .views import *

# some-article

urlpatterns = [
    path('', posts_list, name='posts_list_url'),
    path('post/create/', PostCreate.as_view(), name='post_create_url'),
    path('post/<int:id>/', PostDetail.as_view(), name='post_detail_url'),
    path('post/<int:id>/post_liked/', PressLike.as_view(), name='post_like_url'),
    path('post/<int:id>/update/', PostUpdate.as_view(), name='post_update_url'),
    path('post/<int:id>/delete/', PostDelete.as_view(), name='post_delete_url'),
    path('tags/', tag_list, name='tag_list_url'),
    path('tag/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<int:id>/', TagDetail.as_view(), name='tag_detail_url'),
    path('tag/<int:id>/update/', TagUpdate.as_view(), name='tag_update_url'),
    path('tag/<int:id>/delete/', TagDelete.as_view(), name='tag_delete_url'),
]