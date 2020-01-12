from django.forms import ModelForm
from django import forms
from .models import Post, ImageTag
from django.forms import TextInput, EmailField
from django.core.exceptions import ValidationError


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'project_image', 'technologists', 'description']


class ContactForm(forms.Form):
    subject = forms.CharField(widget=forms.TextInput, max_length=100)
    message = forms.CharField(widget=forms.TextInput, max_length=300)


class AddImageForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['project_image']


class AddTechnologyForm(forms.ModelForm):
    class Meta:
        model = ImageTag
        fields = ['image']


class ImageTagForm(ModelForm):
    class Meta:
        model = ImageTag
        fields = ['image']
