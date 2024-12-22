# load_app/urls.py
from django.urls import path
from .views import generate_load, check_status, create_user

urlpatterns = [
    path('generate-load', generate_load, name='generate_load'),
    path('check-status/<str:auth_uuid>', check_status, name='check_status'),
    path('create-user', create_user, name='create_user'),
]