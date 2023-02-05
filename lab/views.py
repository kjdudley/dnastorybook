from django.shortcuts import render

# Create your views here.
def labhome(request):
    return render(request, 'lab/labhome.html')
