# Generated by Django 4.1.3 on 2023-01-29 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_alter_widget_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='widget',
            name='x',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='widget',
            name='y',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
