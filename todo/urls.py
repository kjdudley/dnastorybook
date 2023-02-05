from django.urls import path
from todo import views

urlpatterns = [
    path('createtodo/', views.createtodo, name='createtodo'),
    path('', views.currenttodos, name='currenttodos'),
    path('completed/', views.completedtodos, name='completedtodos'),
    path('<int:todo_pk>', views.viewtodo, name='viewtodo'),
    path('<int:todo_pk>/complete', views.completetodo, name='completetodo'),
    path('<int:todo_pk>/delete', views.deletetodo, name='deletetodo'),
]
