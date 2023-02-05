from django.shortcuts import render

# Create your views here.
def jbrowse(request):
    return render(request, 'jbrowse/jbrowse.html')
