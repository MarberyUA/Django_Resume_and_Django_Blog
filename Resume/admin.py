from django.contrib import admin
from .models import GitHubProfile, Email

# Register your models here.

admin.site.register(GitHubProfile)
admin.site.register(Email)