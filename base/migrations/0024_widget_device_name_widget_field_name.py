# Generated by Django 4.1.3 on 2023-02-02 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0023_alter_widget_h_alter_widget_type_alter_widget_w'),
    ]

    operations = [
        migrations.AddField(
            model_name='widget',
            name='device_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='widget',
            name='field_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]