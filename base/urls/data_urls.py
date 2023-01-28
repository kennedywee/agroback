from django.urls import path
from . import views

urlpatterns = [
    # Read Data
    path('read/', views.DataList.as_view(), name='data-list'),

    # Update Data
    path('write/', views.CreateData.as_view(), name='data-add'),
]
