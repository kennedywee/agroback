# Generated by Django 4.1.3 on 2023-01-27 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='location',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]