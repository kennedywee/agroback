from django.contrib import admin
from .models import Device, Data, Widget, Alert, Schedule

# Register your models here.
admin.site.register(Device)
admin.site.register(Data)
admin.site.register(Widget)
admin.site.register(Alert)
admin.site.register(Schedule)
