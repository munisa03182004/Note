import uuid
from django.db import models

from app_users.models import User


class Note(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)
    is_done = models.TextField(null=True,blank=True)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title