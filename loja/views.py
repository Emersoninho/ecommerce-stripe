from django.shortcuts import render
from .models import Product

def Produc_detail(request, slug):
    return render(request, 'loja/produtos_detalhes.html')