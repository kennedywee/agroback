# Generated by Django 4.1.3 on 2023-02-02 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0024_widget_device_name_widget_field_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='condition_value',
            field=models.FloatField(max_length=20),
        ),
    ]
