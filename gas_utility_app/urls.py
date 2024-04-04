# gas_utility_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_service_request, name='submit_service_request'),
    path('status/', views.request_status, name='request_status'),
]
