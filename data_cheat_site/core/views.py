from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Course, Contributor
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic

#from django.urls import reverse

# Create your views here.

class IndexView(generic.ListView):
    template_name = "core/index.html"
    context_object_name = "course_list"

    def get_queryset(self):
        return Course.objects.all()

class ContributorsView(generic.ListView):
    template_name = "core/about.html"
    context_object_name = "contributors"
    
    def get_queryset(self):
        return Contributor.objects.all()
