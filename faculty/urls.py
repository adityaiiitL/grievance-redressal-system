from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('report/', views.report, name="report"),
    path('read/<int:id>', views.read, name='read'),
    path('reports/', views.reports, name="reports"),
    path('complain/', views.Complain_, name="complain"),
]