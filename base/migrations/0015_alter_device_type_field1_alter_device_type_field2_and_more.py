# Generated by Django 4.1.3 on 2023-01-30 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_device_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='type_field1',
            field=models.CharField(choices=[('data', 'DataField'), ('temperature', 'HumiditySensor'), ('soil', 'LightSensor'), ('humidity', 'TemperatureSensor'), ('relay', 'Relay')], default='data', max_length=20),
        ),
        migrations.AlterField(
            model_name='device',
            name='type_field2',
            field=models.CharField(choices=[('data', 'DataField'), ('temperature', 'HumiditySensor'), ('soil', 'LightSensor'), ('humidity', 'TemperatureSensor'), ('relay', 'Relay')], default='data', max_length=20),
        ),
        migrations.AlterField(
            model_name='device',
            name='type_field3',
            field=models.CharField(choices=[('data', 'DataField'), ('temperature', 'HumiditySensor'), ('soil', 'LightSensor'), ('humidity', 'TemperatureSensor'), ('relay', 'Relay')], default='data', max_length=20),
        ),
        migrations.AlterField(
            model_name='device',
            name='type_field4',
            field=models.CharField(choices=[('data', 'DataField'), ('temperature', 'HumiditySensor'), ('soil', 'LightSensor'), ('humidity', 'TemperatureSensor'), ('relay', 'Relay')], default='data', max_length=20),
        ),
        migrations.AlterField(
            model_name='device',
            name='type_field5',
            field=models.CharField(choices=[('data', 'DataField'), ('temperature', 'HumiditySensor'), ('soil', 'LightSensor'), ('humidity', 'TemperatureSensor'), ('relay', 'Relay')], default='data', max_length=20),
        ),
    ]