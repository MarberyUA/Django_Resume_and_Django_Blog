from django.forms import ModelForm
from django import forms
from .models import Post, ImageTag, GitHubProfile, Email
from django.forms import TextInput, EmailField
from django.core.exceptions import ValidationError


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'project_image', 'technologists', 'description']

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug must be unique. We have "{}" slug already'.format(new_slug))

        return new_slug


class ContactForm(forms.Form):
    subject = TextInput()
    message = TextInput()


class AddImageForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['project_image']


class AddTechnologyForm(forms.ModelForm):
    class Meta:
        model = ImageTag
        fields = ['slug', 'image']


class ImageTagForm(ModelForm):
    class Meta:
        model = ImageTag
        fields = ['slug', 'image']

    def clean_slug(self):

        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug must be unique. We have "{}" slug already'.format(new_slug))

        return new_slug


class GitHubUpdateForm(ModelForm):
    class Meta:
        model = GitHubProfile
        fields = ['link']


class EmailUpdateForm(ModelForm):
    class Meta:
        model = Email
        fields = ['email', 'email_password', 'email_host', 'email_port', 'email_ssl', 'email_tls']