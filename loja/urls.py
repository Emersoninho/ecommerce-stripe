from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('add_to_carrinho/<int:product_id>/', views.add_to_carrinho, name='add_to_carrinho'),
    path('cart/', views.carrinho_view, name='carrinho_view'),
    path('<slug:slug>/', views.category_detail, name='category_detail'),
    path('<slug:category_slug>/<slug:slug>/', views.Product_detail, name='product_detail'),
]
