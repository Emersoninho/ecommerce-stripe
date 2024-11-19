from django.urls import path
from . import views

urlpatterns = [
    path('vendors/<int:pk>/', views.vendor_details, name='vendor_details')
]
