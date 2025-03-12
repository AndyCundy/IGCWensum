from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import ListView, UpdateView, DeleteView, DetailView
from datetime import datetime, time, date

from django.db.models import Sum

from .models import Course, Hole


# Create your views here.


# Display a list of the courses in the database
#class CourseList(ListView):
#   model = Course
#   context_object_name = 'course_list'

def course_list(request):
    course = Course.objects.all()
    return render(request, 'courses/course_list.html', { 'course_list' : course})

def wensum_detail(request):
    holes = Hole.objects.filter(course__name='Wensum - Wensum Course').order_by('number')
    return render(request, 'courses/wensum_detail.html', { 'wensum_details' : holes})

def valley_detail(request):   
    holes = Hole.objects.filter(course__name='Wensum - Valley Course').order_by('number')
    return render(request, 'courses/valley_detail.html', { 'valley_details' : holes})
