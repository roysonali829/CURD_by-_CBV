from django.shortcuts import render

from app.models import *
from django.views.generic import ListView,TemplateView,DetailView

# Create your views here.

class Schoollist(ListView):
    model = School
    context_object_name = 'students'

# class Home(TemplateView):
#     template_name = 'app/home.html'

class Home(TemplateView):
    template_name='app/home.html'

class Schooldetail(DetailView):
    model = School
    context_object_name = 'schoolobj'