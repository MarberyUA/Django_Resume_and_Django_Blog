from django.contrib.auth.forms import UserCreationForm
from accounts import models


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = models.User
        fields = UserCreationForm.Meta.fields + ('email',)