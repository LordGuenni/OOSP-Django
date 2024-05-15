from django.urls import path
from . import views

urlpatterns = [
    path("", views.subnet_view, name='subnet_view'),
    path('details/', views.subnet_details_view, name='subnet_details'),
    path('create/', views.subnet_create_view, name='subnet_create'),
    path('devices/gen/', views.device_create_view, name='device_new'),
     path('devices/', views.device_list_view, name='device_list'),
]