from django.urls import path
from base.views import widget_views as views

urlpatterns = [
    path('', views.getMyWidgets, name='widgets'),

]
