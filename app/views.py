from django.shortcuts import render

from app.models import *
from django.views.generic import ListView

# Create your views here.

class Schoollist(ListView):
    model = School
    context_object_name = 'students'