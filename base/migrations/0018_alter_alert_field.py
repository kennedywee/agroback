# Generated by Django 4.1.3 on 2023-01-31 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_alter_alert_options_remove_alert_activition_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='field',
            field=models.CharField(max_length=20),
        ),
    ]
