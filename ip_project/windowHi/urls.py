from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('first', views.first),
    path('second', views.second),
]