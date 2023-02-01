from django.urls import path
from base.views import schedule_views as views


urlpatterns = [

    # Frontend
    path('', views.getMySchedules, name='schedules'),
    path('<str:pk>', views.getSchedule, name='schedule'),
    path('create/', views.createSchedule, name='schedules-create'),
    path('update/<str:pk>/', views.updateSchedule, name='schedules-update'),
    path('delete/<str:pk>/', views.deleteSchedule, name='schedules-delete'),
]
