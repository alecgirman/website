from django.shortcuts import render
from django.http import HttpResponse

from os import system

# Create your views here.

def index(request):
    return HttpResponse('<h1>HTTP 200 Everything works!</h1>')

def gitpull(request):
    system('echo git pull')
    return HttpResponse('<h1>Tried git pull...</h1>')
