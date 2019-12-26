from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts import models


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = models.User
        fields = UserCreationForm.Meta.fields + ('email',)


# class (UserChangeForm):
#
#     class Meta:
#         model = models.User
#         fields = UserChangeForm.Meta.fields

