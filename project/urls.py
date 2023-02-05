from django.urls import path
from project import views

urlpatterns = [
    path('createproject/', views.createproject, name='createproject'),
    path('', views.currentprojects, name='currentprojects'),
    path('completed/', views.completedprojects, name='completedprojects'),
#    path('<int:project_pk>', views.viewproject, name='viewproject'),
#    path('<int:project_pk>/complete', views.completeproject, name='completeproject'),
]
