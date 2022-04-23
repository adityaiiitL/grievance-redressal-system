from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('report/', views.report, name="report"),
    path('read/<int:id>', views.read, name='read'),
    path('complainform/', views.complainform, name='complainform')
]