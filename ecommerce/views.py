from django.shortcuts import render
from loja.models import Product

def frontpage(request):
    products = Product.objects.all()[0:6]
    return render(request, 'ecommerce/frontpage.html', {'products': products})

def sobre(request):
    return render(request, 'ecommerce/sobre.html')