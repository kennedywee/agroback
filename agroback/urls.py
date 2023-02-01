from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('base.urls.user_urls')),
    path('api/devices/', include('base.urls.device_urls')),
    path('api/data/', include('base.urls.data_urls')),
    path('api/widgets/', include('base.urls.widget_urls')),
    path('api/alerts/', include('base.urls.alert_urls')),
    path('api/schedules/', include('base.urls.schedule_urls')),
]
