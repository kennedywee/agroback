from django.contrib import admin
from .models import Device, Data, Widget

# Register your models here.
admin.site.register(Device)
admin.site.register(Data)
admin.site.register(Widget)
