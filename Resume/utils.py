from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

class ObjectDetailMixin:
    template = None
    model = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})