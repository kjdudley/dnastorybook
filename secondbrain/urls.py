"""secondbrain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from note import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),

    # Home
    path('', views.home, name='home'),

    # Link to Dashboard App URLs
    path('dashboard/', include('dashboard.urls')),

    # Link to Note App URLs
    path('notes/', include('note.urls'), name='notes'),

    # Link to Todo App URLs
    path('todos/', include('todo.urls'), name='todos'),

    # Link to Project App URLs
    path('projects/', include('project.urls'), name='projects'),

    # Link to Lab App URLs
    path('lab/', include('lab.urls'), name='lab'),

    # Link to Protocol App URLs
    path('protocols/', include('protocol.urls')),

    # Link to Quotegenerator App URLs
    path('tools/quote/', include('quotegenerator.urls'), name='quotegenerator'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
