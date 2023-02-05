from django.urls import path
from protocol import views

urlpatterns = [
    path('newprotocol/', views.newprotocol, name='newprotocol'),
#    path('newprotocol/create/', views.createprotocol, name='createprotocol'),
    path('', views.currentprotocols, name='currentprotocols'),
    path('<int:prv_fk>/', views.selectedprotocol, name='selectedprotocol'),
]
