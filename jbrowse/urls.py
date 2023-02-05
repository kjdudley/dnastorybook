from django.urls import path
from jbrowse import views

urlpatterns = [
    path('', views.jbrowse, name='jbrowse'),
]
