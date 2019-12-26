from django.shortcuts import redirect
from django.http import HttpResponse


def redirect_resume(request):
    return redirect('about_me_url', permanent=True)
