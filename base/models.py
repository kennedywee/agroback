from django.db import models
from django.contrib.auth.models import User
import string
import random

API_KEY_LENGTH = 20


# Create your models here.

class Device(models.Model):

    class FieldTypes(models.TextChoices):
        DATA = 'data', ('DataField')
        TEMPERATURE = 'temperature', ('HumiditySensor')
        LIGHT = 'soil', ('LightSensor')
        HUMIDITY = 'humidity', ('TemperatureSensor')
        RELAY = 'relay', ('Relay')

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=60)
    device_type = models.CharField(max_length=60)
    location = models.CharField(max_length=60, null=True, blank=True)

    active = models.BooleanField(default=False)

    field1 = models.CharField(max_length=20, null=True, blank=True)
    field2 = models.CharField(max_length=20, null=True, blank=True)
    field3 = models.CharField(max_length=20, null=True, blank=True)
    field4 = models.CharField(max_length=20, null=True, blank=True)
    field5 = models.CharField(max_length=20, null=True, blank=True)

    type_field1 = models.CharField(max_length=20,
                                   choices=FieldTypes.choices,
                                   default=FieldTypes.DATA)
    type_field2 = models.CharField(max_length=20,
                                   choices=FieldTypes.choices,
                                   default=FieldTypes.DATA)
    type_field3 = models.CharField(max_length=20,
                                   choices=FieldTypes.choices,
                                   default=FieldTypes.DATA)
    type_field4 = models.CharField(max_length=20,
                                   choices=FieldTypes.choices,
                                   default=FieldTypes.DATA)
    type_field5 = models.CharField(max_length=20,
                                   choices=FieldTypes.choices,
                                   default=FieldTypes.DATA)

    description = models.TextField(max_length=200, null=True, blank=True)

    api_key = models.CharField(
        max_length=API_KEY_LENGTH, unique=True, null=False, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name

    def generate_api():
        while True:
            api_key = ''.join(random.choices(
                string.ascii_lowercase + string.digits, k=API_KEY_LENGTH))

            # break if theres no same api under
            if Device.objects.filter(api_key=api_key).count() == 0:
                break

        return api_key

    def save(self, *args, **kwargs):
        if not self.api_key:
            self.api_key = Device.generate_api()

        return super().save(*args, **kwargs)


class Data(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    field1 = models.FloatField(null=True, blank=True)
    field2 = models.FloatField(null=True, blank=True)
    field3 = models.FloatField(null=True, blank=True)
    field4 = models.FloatField(null=True, blank=True)
    field5 = models.FloatField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.device.name


class Alert(models.Model):

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=20)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    field = models.IntegerField(null=False, blank=False)
    condition_value = models.IntegerField(null=False, blank=False)
    message = models.TextField(max_length=200)
    frequency = models.BooleanField(default=False)
    activition = models.IntegerField(null=False, blank=False)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name


class FieldTypes(models.TextChoices):
    NEW = 'newchart', ('New Chart')
    LINECHART = 'linechart', ('Line Chart')
    GAUGE = 'gauge', ('Gauge Chart')
    SWITCH = 'switch', ('Switch Control')
    INDICATOR = 'indicator', ('Indicator Chart')
    PERCENTAGE = 'percentage', ('Percentage Chart')


class Widget(models.Model):

    i = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    type = models.CharField(
        max_length=20, choices=FieldTypes.choices, default=FieldTypes.NEW)
    device = models.ForeignKey(
        Device, on_delete=models.SET_NULL, null=True, blank=True)
    datafield = models.CharField(max_length=20, blank=True)
    w = models.IntegerField(null=True, blank=True)
    h = models.IntegerField(null=True, blank=True)
    y = models.IntegerField(default=0, null=False, blank=True)
    x = models.IntegerField(default=0, null=False, blank=True)
    maxH = models.IntegerField(null=True, blank=True)
    minH = models.IntegerField(null=True, blank=True)
    maxW = models.IntegerField(null=True, blank=True)
    minW = models.IntegerField(null=True, blank=True)
    moved = models.BooleanField(default=False)
    static = models.BooleanField(default=False)
    isResizable = models.BooleanField(default=True)

    def __str__(self):
        return self.type

    def save(self, *args, **kwargs):
        if self.pk is None:
            if self.type == FieldTypes.NEW:
                self.maxH = 11
                self.maxW = 12
                self.minH = 8
                self.minW = 7
                self.w = 8
                self.h = 7

            elif self.type == FieldTypes.LINECHART:
                self.maxH = 11
                self.maxW = 12
                self.minH = 8
                self.minW = 7
                self.w = 8
                self.h = 7

            elif self.type == FieldTypes.GAUGE:
                self.maxH = 5
                self.maxW = 3
                self.minH = 5
                self.minW = 3
                self.w = 3
                self.h = 5

            elif self.type == FieldTypes.SWITCH:
                self.maxH = 5
                self.maxW = 3
                self.minH = 4
                self.minW = 2
                self.w = 2
                self.h = 4

            elif self.type == FieldTypes.INDICATOR:
                self.maxH = 5
                self.maxW = 3
                self.minH = 4
                self.minW = 2
                self.w = 2
                self.h = 4

            elif self.type == FieldTypes.PERCENTAGE:
                self.maxH = 5
                self.maxW = 3
                self.minH = 5
                self.minW = 3
                self.w = 3
                self.h = 5

        return super().save(*args, **kwargs)
