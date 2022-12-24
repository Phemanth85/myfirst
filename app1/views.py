from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hemanth(request):
    return HttpResponse('<marquee><h1>It is my first Project</h1></marquee>')