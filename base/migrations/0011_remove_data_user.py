# Generated by Django 4.1.3 on 2023-01-29 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_data_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='user',
        ),
    ]