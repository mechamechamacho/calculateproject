from django.contrib import admin
from django.urls import path
from .views import Creator
from . import views

urlpatterns = [
    path('calculate/', Creator.as_view(), name='creator'),
]
