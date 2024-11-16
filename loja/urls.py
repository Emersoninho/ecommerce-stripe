from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.Produc_detail, name='product_detail'),
]
