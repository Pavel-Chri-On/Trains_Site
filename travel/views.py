from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    name = 'Anybody'
    return render(request, 'home.html', {'name': name})


def about(request):
    name = 'Anybody'
    return render(request, 'about.html', {'name': name})