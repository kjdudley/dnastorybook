from django.urls import path
from quotegenerator import views

urlpatterns = [
    path('', views.quote, name='getquote'),
    path('viewquote/', views.viewquote, name='viewquote'),
]
