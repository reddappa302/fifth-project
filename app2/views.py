from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def red(request):
    return HttpResponse('<h1>this is the first response from second application</h1>')

def green(request):
    return HttpResponse('<h2><marquee>this is the second response of application 2</marquee></h2>')