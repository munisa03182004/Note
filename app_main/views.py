from django.shortcuts import render, redirect,get_object_or_404

from django.contrib.auth import get_user_model
from .forms import Note


User= get_user_model()

def home_page(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'app_main/note.html')

def employees(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if not request.user.is_staff and not request.user.is_superuser:
        return redirect('note')

    employees_list = User.objects.all()

    context = {
        'employees': employees_list
    }

    return render(request, 'app_main/employees.html', context)


