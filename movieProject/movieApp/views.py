from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return HttpResponse("welcome")


def indexDirection(request):
    print("test")
    # return HttpResponse("Test")
    return render(request, 'movieApp/index.html')


def Base(request):
    return render(request, 'movieApp/Base.html')


def About(request):
    return render(request, 'movieApp/About.html')
