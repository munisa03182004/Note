from django.shortcuts import render, redirect,get_object_or_404

from django.contrib.auth import get_user_model
from .forms import Note, Note

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

def add_note(request):
    if request.method == 'POST':
        form = Note(request.POST)
        if form.is_valid():
            # Set the owner_id field before saving the form
            form.instance.owner_id = request.user
            form.save()
            return redirect('home')  # Redirect to home page after adding note
    else:
        form = Note()
    return render(request, 'app_main/add_note.html', {'form': form})

def update_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        form = Note(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home page after updating note
    else:
        form = Note(instance=note)
    return render(request, 'app_main/update_note.html', {'form': form, 'note': note})