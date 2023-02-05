from django.conf import settings
from django.core.mail import send_mail
from datetime import timedelta
from django.db import models
from django.contrib.auth.models import User
import string
import random
API_KEY_LENGTH = 20


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
    active = models.BooleanField(default=True)

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
    field1 = models.FloatField(default=0.0, null=True, blank=True)
    field2 = models.FloatField(default=0.0, null=True, blank=True)
    field3 = models.FloatField(default=0.0, null=True, blank=True)
    field4 = models.FloatField(default=0.0, null=True, blank=True)
    field5 = models.FloatField(default=0.0, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.device.name

    def check_alert(self):
        # check if there is any active alert associated with the device
        alerts = Alert.objects.filter(device=self.device, active=True)

        if alerts.exists():
            for alert in alerts:
                field_value = getattr(self, alert.field)

                print(type(field_value))

                print(type(alert.condition_value))

                print(float(field_value) == float(alert.condition_value))

                if float(field_value) == float(alert.condition_value):

                    print("yes boss")

                    email_host = settings.EMAIL_HOST_USER

                    subject = 'Alert triggered: {}'.format(alert.name)
                    message = 'The alert {} has been triggered for device {}. The message is: {}'.format(
                        alert.name,
                        alert.device,
                        alert.message
                    )
                    recipient_list = [alert.user.email]
                    send_mail(subject, message, email_host, recipient_list)
                    print(alert.user.email)

                    print("yes boss")

                    print("yes boss", flush=True)
                    alert.active = False
                    alert.save()

    def save(self, *args, **kwargs):
        # latest_data = Data.objects.filter(
        #     device=self.device).order_by('-created').first()
        # self.field1 = self.field1 or (
        #     latest_data.field1 if latest_data else None)
        # self.field2 = self.field2 or (
        #     latest_data.field2 if latest_data else None)
        # self.field3 = self.field3 or (
        #     latest_data.field3 if latest_data else None)
        # self.field4 = self.field4 or (
        #     latest_data.field4 if latest_data else None)
        # self.field5 = self.field5 or (
        #     latest_data.field5 if latest_data else None)
        if self.pk is None:
            self.check_alert()
            print("checking alert")
            print("checking alert", flush=True)
        super().save(*args, **kwargs)


class Alert(models.Model):

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=20)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    field = models.CharField(max_length=20)
    condition_value = models.FloatField(max_length=20)
    message = models.TextField(max_length=200)
    frequency = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class FieldTypes(models.TextChoices):
    LINECHART = 'linechart', ('Line Chart')
    GAUGE = 'gauge', ('Gauge Chart')
    SWITCH = 'switch', ('Switch Control')
    INDICATOR = 'indicator', ('Indicator Chart')
    PERCENTAGE = 'percentage', ('Percentage Chart')


class Widget(models.Model):

    i = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    type = models.CharField(
        max_length=20, choices=FieldTypes.choices, default=FieldTypes.LINECHART)
    device = models.ForeignKey(
        Device, on_delete=models.CASCADE, null=True, blank=True)
    datafield = models.CharField(max_length=20, blank=True)
    device_name = models.CharField(max_length=100, null=True, blank=True)
    field_name = models.CharField(max_length=100, null=True, blank=True)
    w = models.IntegerField(null=True, blank=False)
    h = models.IntegerField(null=True, blank=False)
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

            if self.type == FieldTypes.LINECHART:
                self.maxH = 11
                self.maxW = 12
                self.minH = 8
                self.minW = 6
                self.w = 6
                self.h = 6

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

        if self.device:
            self.device_name = self.device.name
        if self.datafield:
            fields = [self.device.field1, self.device.field2,
                      self.device.field3, self.device.field4, self.device.field5]
            field_index = int(self.datafield[-1]) - 1
            self.field_name = fields[field_index]

        return super().save(*args, **kwargs)


class Schedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    duration = models.DurationField()
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    field = models.CharField(max_length=20)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if type(self.duration) == str:
            self.duration = timedelta(hours=int(self.duration.split(':')[0]),
                                      minutes=int(self.duration.split(':')[1]),
                                      seconds=int(self.duration.split(':')[2]))
        super().save(*args, **kwargs)
