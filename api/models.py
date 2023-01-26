import string
import random

from django.db import models
from django.utils.translation import gettext_lazy as _

# Variables
API_KEY_LENGTH = 20

# Model for Device


class Device(models.Model):

    # field types choices
    class FieldTypes(models.TextChoices):
        DATA = 'DF', ('DataField')
        HUMIDITY = 'HS', ('HumiditySensor')
        LIGHT = 'LS', ('LightSensor')
        TEMPERATURE = 'TS', ('TemperatureSensor')
        RELAY = 'RY', ('RELAY')

    # device name
    name = models.CharField(max_length=60)

    # user (device belong to who)?

    # field names
    field1 = models.CharField(max_length=20, null=True, blank=True)
    field2 = models.CharField(max_length=20, null=True, blank=True)
    field3 = models.CharField(max_length=20, null=True, blank=True)
    field4 = models.CharField(max_length=20, null=True, blank=True)
    field5 = models.CharField(max_length=20, null=True, blank=True)

    # field types
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

    # device description
    description = models.TextField(max_length=200, null=True, blank=True)

    # api key for rest framework
    api_key = models.CharField(
        max_length=API_KEY_LENGTH, unique=True, null=False, blank=True)

    # history
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # class meta: ordering order
    class Meta:
        ordering = ['-created']

    # for readibility
    def __str__(self):
        return self.name

    # generate random api for rest framework
    def generate_api():
        while True:
            api_key = ''.join(random.choices(
                string.ascii_lowercase + string.digits, k=API_KEY_LENGTH))

            # break if theres no same api under
            if Device.objects.filter(api_key=api_key).count() == 0:
                break

        return api_key

    # default generate api during save

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
