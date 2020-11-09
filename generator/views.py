from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'generator/home.html')

def password(request):

    thepassword = ''
    characters = [x for x in 'abcdefghijklmnopqrstuvwxyz']

    if request.GET.get('uppercase'):
        characters.extend([x.upper() for x in characters])

    if request.GET.get('special'):
        characters.extend([x for x in '@#$%^*&?'])

    # if request.GET.get('numbers'):
    #     characters.extend(list(range(0,10)))

    length = int(request.GET.get('length',12))

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request,'generator/password.html',{'password':thepassword})

def about(request):
    return render(request,'generator/about.html')
