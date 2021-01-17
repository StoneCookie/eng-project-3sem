from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from main.models import *

def index(request):
    return render(request, 'windowHi/index.html')

def first(request):
    cmpData = Company.objects.all()
    return render(request, "windowHi/first.html", {"cmpData": cmpData})

def second(request):
    vacData = Vacancy.objects.all()
    return render(request, "windowHi/second.html", {"vacData": vacData})