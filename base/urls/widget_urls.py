from django.urls import path
from base.views import widget_views as views

urlpatterns = [
    path('', views.getMyWidgets, name='widgets'),
    path('update/<str:pk>/', views.updateWidget, name='widgets-update'),
    path('create/', views.createWidget, name='widgets-create'),

]
