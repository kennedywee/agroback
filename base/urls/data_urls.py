from django.urls import path
from base.views import data_views as views


urlpatterns = [

    # Fronted
    path('read/<str:pk>/', views.getMyData, name='frontdata-list'),
    path('create/', views.createData, name='frontdata-create'),


    # Dashboard
    path('dashboard/', views.getDashboardData, name='dashboard-data-list'),

    # Microcontroller
    path('read/', views.DataList.as_view(), name='data-list'),
    path('write/', views.CreateData.as_view(), name='data-add'),


    # Agroscheduler
    path('agroscheduler/<str:pk>/', views.agroScheduler, name='agroscheduler'),
]
