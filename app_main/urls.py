from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('employees/', views.employees, name='employees'),
    path('add/', views.add_note, name='add_note'),
    path('update/<uuid:note_id>/', views.update_note, name='update_note'),
]
