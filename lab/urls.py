from django.urls import path
from lab import views

urlpatterns = [
    path('', views.labhome, name='labhome'),
 ]
