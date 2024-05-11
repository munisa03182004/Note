from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('employees/',views.employees, name='employees'),
]
