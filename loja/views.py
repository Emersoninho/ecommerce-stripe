from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Category.products.all()
    return render(request, 'loja/category_detalhes.html', {'category': category, 'products': products})

def Product_detail(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'loja/produtos_detalhes.html', {'product': product})
