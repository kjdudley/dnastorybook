from django.urls import path
from note import views

urlpatterns = [
    path('create/', views.createnote, name='createnote'),
    path('', views.livenotes, name='livenotes'),
    path('resourcenotes/', views.resourcenotes, name='resourcenotes'),
    path('<int:note_pk>', views.viewnote, name='viewnote'),
    path('<int:note_pk>/resourcenote', views.resourcenote, name='resourcenote'),
]

