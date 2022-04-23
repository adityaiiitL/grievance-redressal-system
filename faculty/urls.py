from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('report/', views.report, name="report"),
    path('complainform/', views.complainform,name="complain_f"),
    path('read/<int:id>', views.read, name='read'),
<<<<<<< HEAD
    path('complainform/', views.complainform, name='complainform')
=======
    path('reports/', views.reports, name="reports"),
    path('complain/', views.Complain_, name="complain"),
>>>>>>> bef1943ef1d78e3eafc11a41d738ab6bb20e117c
]