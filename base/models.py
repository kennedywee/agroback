from django.db import models
from django.contrib.auth.models import User
import string
import random

API_KEY_LENGTH = 20


# Create your models here.

class Device(models.Model):

    class FieldTypes(models.TextChoices):
        DATA = 'DF', ('DataField')
        HUMIDITY = 'HS', ('HumiditySensor')
        LIGHT = 'LS', ('LightSensor')
        TEMPERATURE = 'TS', ('TemperatureSensor')
        RELAY = 'RY', ('RELAY')

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=60)
    device_type = models.CharField(max_length=60)
    location = models.CharField(max_length=60, null=True, blank=True)

    field1 = models.CharField(max_length=20, null=True, blank=True)
    field2 = models.CharField(max_length=20, null=True, blank=True)
    field3 = models.CharField(max_length=20, null=True, blank=True)
    field4 = models.CharField(max_length=20, null=True, blank=True)
    field5 = models.CharField(max_length=20, null=True, blank=True)

    type_field1 = models.CharField(max_length=2,
                                   choices=FieldTypes.choices,
                                   default=FieldTypes.DATA)
    type_field2 = models.CharField(max_length=2,
                                   choices=FieldTypes.choices,
                                   default=FieldTypes.DATA)
    type_field3 = models.CharField(max_length=2,
                                   choices=FieldTypes.choices,
                                   default=FieldTypes.DATA)
    type_field4 = models.CharField(max_length=2,
                                   choices=FieldTypes.choices,
                                   default=FieldTypes.DATA)
    type_field5 = models.CharField(max_length=2,
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
    field1 = models.CharField(max_length=10, null=True, blank=True)
    field2 = models.CharField(max_length=10, null=True, blank=True)
    field3 = models.CharField(max_length=10, null=True, blank=True)
    field4 = models.CharField(max_length=10, null=True, blank=True)
    field5 = models.CharField(max_length=10, null=True, blank=True)

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
