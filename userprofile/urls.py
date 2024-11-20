from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('login/', auth_views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('minhaconta/', views.minha_conta, name='minhaconta'),
    path('loja/', views.minha_loja, name='loja'),
    path('loja/add-product/', views.add_product, name='add_product'),
    path('vendors/<int:pk>/', views.vendor_details, name='vendor_details'),
  
]
