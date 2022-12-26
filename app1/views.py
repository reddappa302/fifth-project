from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('<h1>this is the first response of application 1</h1>')

def second(request):
    return HttpResponse('<h1 color=red>this is the second response of application 1</h1>')