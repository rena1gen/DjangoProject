from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "mainApp/html/data.html")


def about(request):
    return render(request, "mainApp/html/about.html")
