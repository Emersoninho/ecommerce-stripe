from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.db.models import Q

def search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    return render(request, 'loja/search.html', {'query': query, 'products': products})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()
    return render(request, 'loja/category_detalhes.html', {'category': category, 'products': products})

def Product_detail(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'loja/produtos_detalhes.html', {'product': product})
