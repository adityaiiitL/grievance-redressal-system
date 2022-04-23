from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
<<<<<<< HEAD
    path('report/', views.report, name="report"),
    path('read/<int:id>', views.read, name='read'),
=======
    path('reports/', views.reports, name="reports"),
    path('complain/', views.Complain_, name="complain"),
>>>>>>> 90957059a6bfcda9ecef85c21ca00fd55cb0ea87
]