from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from . import forms
# Create your views here.

class AddingView(TemplateView):
    template_name = "suma.html"
    def get_context_data(self, *args, **kwargs):
        context = super(AddingView, self).get_context_data(*args, **kwargs)
        form = forms.AddingForm()
        context.update({"form": form})
        return  context
    
    def post(self, *args, **kwargs):
        sumandos = forms.AddingForm(self.request.POST)
        context = self.get_context_data()
        if sumandos.is_valid():
            s1 = sumandos.cleaned_data["s1"]
            s2 = sumandos.cleaned_data["s2"]
            result = int(s1) + int(s2)
            context.update({"result": result})
        return render(self.request, self.template_name, context)
        

