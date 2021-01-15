from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('company/', CompanyListView.as_view()),
    path('', views.index),
    path('about', views.about),
    path('mains/create/', CompanyCreateView.as_view()),
    path('detail/<int:pk>/', CompanyDetailView.as_view()),
]
