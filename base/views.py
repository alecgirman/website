from django.shortcuts import render
from django.http import HttpResponse

from os import system

# Create your views here.

def index(request):
    content = '<h1>HTTP 200 Everything works!</h1>'
    content += '<br />'
    content += '<p>Did this text update</p>'
    return HttpResponse(content)

# when requested, performs a git pull
# this will be changed in the future to be more secure
# NOTE: requires git merge before running
def gitpull(request):
    system('git pull')
    return HttpResponse('<h1>Performed git pull, django should refresh automatically</h1>')
