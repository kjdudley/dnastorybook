from django.shortcuts import render, get_object_or_404
from .forms import ProjectForm
from django.shortcuts import redirect
from .models import Project
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def currentprojects(request):
    projects = Project.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'project/currentprojects.html', {'projects':projects})

@login_required
def completedprojects(request):
    projects = Project.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'project/completedprojects.html', {'projects':projects})

@login_required
def createproject(request):
    if request.method == 'GET':
        return render(request, 'project/createproject.html', {'form':ProjectForm()})
    else:
        try:
            form = ProjectForm(request.POST)
            newproject = form.save(commit=False)
            newproject.user = request.user
            newproject.save()
            return redirect('currentprojects')
        except ValueError:
            return render(request, 'project/currentprojects.html', {'form':ProjectForm(), 'error':'Bad data. Try again.'})
