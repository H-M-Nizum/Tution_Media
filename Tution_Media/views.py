from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class homeview(TemplateView):
    template_name = 'index.html'

class Aboutview(TemplateView):
    template_name = 'about.html'
class serviceview(TemplateView):
    template_name = 'services.html'
