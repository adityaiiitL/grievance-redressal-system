from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('report/', views.report, name="report"),
    path('complain/', views.Complain_, name="complain"),
]