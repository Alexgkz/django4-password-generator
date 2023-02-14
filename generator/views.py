from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    # length = 10
    length = int(request.GET.get('length', 12))
    characters = list('asdfghjklmnbvcxzqwertyuiop')
    HttpResponse(request.GET.get('uppercase'))
    if request.GET.get('uppercase'):
        characters.extend(list('QWERTYUIOPLKJHGFDSAZXCVBNM'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+-=[]{};:?'))
    if request.GET.get('number'):
        characters.extend(list('1234567890'))

    thepassword = ''
    for x in range(length):
        thepassword +=random.choice(characters)
    return render(request, 'generator/password.html', {'password':thepassword})

def about(request):
    return render(request, 'generator/about.html')
