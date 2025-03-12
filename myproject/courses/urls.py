from django.urls import path, re_path
#from django.conf.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'courses'

from . import views

urlpatterns = [
    path('course_list.html', views.course_list, name='course_list'),
    path('wensum_detail.html', views.wensum_detail, name='wensum_detail'),
    path('valley_detail.html', views.valley_detail, name='valley_detail')     
] 