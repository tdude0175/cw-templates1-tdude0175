from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# simple starting point could add flavor but not worried about it
def index(request):
    return HttpResponse("welcome")

# these 3 views just reference the page based on name, not much new
def indexDirection(request):
    return render(request, 'movieApp/index.html')


def Base(request):
    return render(request, 'movieApp/Base.html')


def About(request):
    return render(request, 'movieApp/About.html')
