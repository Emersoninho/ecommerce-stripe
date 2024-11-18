from django.urls import path
from . import views

urlpatterns = [
    path('venders/<int:pk>/', views.vendor_details, name='vendor_details')
]
