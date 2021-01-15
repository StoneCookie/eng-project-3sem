from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Company
from .serializers import CompanySerializer, CompanyListSerializer


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


class CompanyListView(generics.ListAPIView):
    serializer_class = CompanyListSerializer
    queryset = Company.objects.all()


class CompanyCreateView(generics.CreateAPIView):
    serializer_class = CompanySerializer


class CompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
