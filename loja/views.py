from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from django.db.models import Q
from .carrinho import Carrinho

def add_to_carrinho(request, product_id):
    carrinho = Carrinho(request)
    carrinho.add(product_id)

    return redirect('frontpage')

def carrinho_view(request):
    carrinho = Carrinho(request)

    return render(request, 'loja/carrinho_view.html', {'carrinho': carrinho})

def search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(status=Product.ATIVAR).filter(Q(title__icontains=query) | Q(description__icontains=query))
    return render(request, 'loja/search.html', {'query': query, 'products': products})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.filter(status=Product.ATIVAR)
    return render(request, 'loja/category_detalhes.html', {'category': category, 'products': products})

def Product_detail(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug, status=Product.ATIVAR)
    return render(request, 'loja/produtos_detalhes.html', {'product': product})
