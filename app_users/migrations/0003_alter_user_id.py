# Generated by Django 5.0.4 on 2024-05-12 19:21

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0002_alter_user_options_user_date_joined_user_groups_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]