# Generated by Django 4.1.3 on 2023-01-29 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_widget_h_alter_widget_maxh_alter_widget_maxw_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='widget',
            name='isResizable',
            field=models.BooleanField(default=True),
        ),
    ]