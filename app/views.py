from django.shortcuts import render

from .models import *

from django.views.generic import ListView

class WorkerView(ListView):
    model=Worker
    context_object_name= "worker"
    template_name="worker.html"

class WorkersView(ListView):
    model = Worker_about
    context_object_name="work"
    template_name="work_about.html"

from django.views.generic import TemplateView

class menu(TemplateView):
    template_name="index.html"



