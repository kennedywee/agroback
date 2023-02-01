from django.urls import path
from base.views import alert_views as views


urlpatterns = [

    # Frontend
    path('', views.getMyAlerts, name='alerts'),
    path('<str:pk>', views.getAlert, name='alert'),
    path('create/', views.createAlert, name='alerts-create'),
    path('update/<str:pk>/', views.updateAlert, name='alerts-update'),
    path('delete/<str:pk>/', views.deleteAlert, name='alerts-delete'),
]
