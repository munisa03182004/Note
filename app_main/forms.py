from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Note

User = get_user_model()



class Note(ModelForm):
    class Meta:
        model = Note
        fields =['title', 'description', 'is_done']

