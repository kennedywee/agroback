# Generated by Django 4.1.3 on 2023-01-30 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_alter_device_type_field1_alter_device_type_field2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='field1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='field2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='field3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='field4',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='field5',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='widget',
            name='datafield',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='widget',
            name='device',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.device'),
        ),
        migrations.AlterField(
            model_name='widget',
            name='type',
            field=models.CharField(choices=[('newchart', 'New Chart'), ('linechart', 'Line Chart'), ('gauge', 'Gauge Chart'), ('switch', 'Switch Control'), ('indicator', 'Indicator Chart'), ('percentage', 'Percentage Chart')], default='newchart', max_length=20),
        ),
    ]
