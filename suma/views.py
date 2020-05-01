from django.shortcuts import render
from django.views.generic import TemplateView
from . import forms
# Create your views here.

class AddingView(TemplateView):
    template_name = "suma.html"
    def get_context_data(self, *args, **kwargs):
        context = super(AddingView, self).get_context_data(*args, **kwargs)
        form = forms.PlusForm()
        context.update({"form": form})
        return  context