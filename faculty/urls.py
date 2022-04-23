from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('report/', views.report, name="report"),
    path('complainform/', views.complainform,name="complain_f"),
    path('read/<int:id>', views.read, name='read'),
    path('report/', views.report, name="reports"),
    path('complain/', views.Complain_, name="complain"),
]