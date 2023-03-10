# Generated by Django 4.1.3 on 2023-01-31 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_alter_data_field1_alter_data_field2_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alert',
            options={},
        ),
        migrations.RemoveField(
            model_name='alert',
            name='activition',
        ),
        migrations.RemoveField(
            model_name='alert',
            name='created',
        ),
        migrations.AddField(
            model_name='alert',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='alert',
            name='condition_value',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='device',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('datetime', models.DateTimeField()),
                ('duration', models.DurationField()),
                ('field', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.device')),
            ],
        ),
    ]
