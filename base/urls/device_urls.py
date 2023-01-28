from django.urls import path
from base.views import device_views as views

urlpatterns = [
    path('', views.getMyDevices, name='devices'),
    path('<str:pk>', views.getDevice, name='device'),
    path('create/', views.createDevice, name='devices-create'),
    path('update/<str:pk>/', views.updateDevice, name='devices-update'),
    path('delete/<str:pk>/', views.deleteDevice, name='devices-delete'),
]
