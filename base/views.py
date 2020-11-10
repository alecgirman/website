from django.shortcuts import render
from django.http import HttpResponse

from os import system

# Create your views here.

# controls what data is actually sent 
def index(request):
    # render jinja template
    return render(request, 'index.html')

# when requested, performs a git pull
# this will be changed in the future to be more secure
def gitpull(request):
    system('git pull')
    return HttpResponse('<h1>Performed git pull, django should refresh automatically</h1>')
