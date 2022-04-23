from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('reports/', views.reports, name="reports"),
    path('complain/', views.Complain_, name="complain"),
]