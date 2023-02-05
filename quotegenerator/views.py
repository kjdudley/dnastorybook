from django.shortcuts import render
import random

# Create your views here.
def quote(request):
    return render(request, 'quotegenerator/getquote.html')

def viewquote(request):
    numbers = list('0123456789')
    length = int(request.GET.get('readlength', 4))
    thequote = ''
    for x in range(length):
        thequote += random.choice(numbers)
    currency = "$"
    thequote = currency+thequote
    return render(request, 'quotegenerator/viewquote.html', {'quote':thequote})
