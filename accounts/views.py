from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.views import PasswordResetDoneView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.views import View
from .forms import CustomUserCreationForm


# Create your views here.


class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/sign_up.html'


# class ChangePassword(View):
#     def get(self, request):
#         form = PasswordChangeForm(request.user)
#
class ChangeUserDetails(UpdateView):
    form_class = PasswordResetForm
    success_url = reverse_lazy('login')
    template_name = 'registration/password_reset_form.html.html'


class ChangeUserDetailsDone(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'
