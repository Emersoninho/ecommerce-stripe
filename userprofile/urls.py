from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('minhaconta/', views.minha_conta, name='minhaconta'),
    path('vendors/<int:pk>/', views.vendor_details, name='vendor_details'),
  
]
