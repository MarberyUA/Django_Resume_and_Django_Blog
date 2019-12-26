from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', projects_list, name='about_me_url'),
    path('<str:slug>/email_setting/', EmailSettingsUpdate.as_view(), name='email_setting_url'),
    path('<str:slug>/github_setting/', GitHubSettingsUpdate.as_view(), name='github_setting_url'),
    path('send_mail/', contact, name='contact_me_url'),
    path('<str:slug>/pinned_successful/', PinPost.as_view(), name='pin_post_url'),
    path('load_projects/', LoadProjects.as_view(), name='load_projects_url'),
    path('project/create/', ProjectCreate.as_view(), name='project_create_url'),
    path('project/<str:slug>/', ProjectDetail.as_view(), name='project_detail_url'),
    path('project/<str:slug>/edit/', ProjectEdit.as_view(), name='project_edit_url'),
    path('project/<str:slug>/delete/', ProjectDelete.as_view(), name='project_delete_url'),
    path('project/<str:slug>/add_image/', AddImage.as_view(), name='add_project_image_url'),
    path('project/<str:slug>/add_technology/', AddTechnology.as_view(), name='add_technology_url'),
    path('tags/', tag_list, name='tag_list_url'),
    path('tag/create', ImageTagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slug>/', ImageTagDetail.as_view(), name='tag_detail_url'),
    path('tag/<str:slug>/delete/', ImageTagDelete.as_view(), name='tag_delete_url'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)