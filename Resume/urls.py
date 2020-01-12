from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', ProjectsList.as_view(), name='about_me_url'),
    path('<int:id>/pinned_successful/', PinPost.as_view(), name='pin_post_url'),
    path('load_projects/', LoadProjects.as_view(), name='load_projects_url'),
    path('project/create/', ProjectCreate.as_view(), name='project_create_url'),
    path('project/<int:id>/', ProjectDetail.as_view(), name='project_detail_url'),
    path('project/<int:id>/edit/', ProjectEdit.as_view(), name='project_edit_url'),
    path('project/<int:id>/delete/', ProjectDelete.as_view(), name='project_delete_url'),
    path('project/<int:id>/add_image/', AddImage.as_view(), name='add_project_image_url'),
    path('project/<int:id>/add_technology/', AddTechnology.as_view(), name='add_technology_url'),
    path('tags/', tag_list, name='tag_list_url'),
    path('tag/create', ImageTagCreate.as_view(), name='tag_create_url'),
    path('tag/<int:id>/', ImageTagDetail.as_view(), name='tag_detail_url'),
    path('tag/<int:id>/delete/', ImageTagDelete.as_view(), name='tag_delete_url'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)