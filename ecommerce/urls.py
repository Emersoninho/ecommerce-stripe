from django.urls import path
from ecommerce import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('sobre/', views.sobre, name='sobre')
]
