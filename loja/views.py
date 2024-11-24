from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Order, OrderItem
from django.db.models import Q
from .carrinho import Carrinho
from django.contrib.auth.decorators import login_required
from .forms import OrderForm

def add_to_carrinho(request, product_id):
    carrinho = Carrinho(request)
    carrinho.add(product_id)

    return redirect('carrinho_view')

def trocar_quantidade(request, product_id):
    action = request.GET.get('action', '')
    if action:
        quantity = 1
        if action == 'decrease':
            quantity = -1
        carrinho = Carrinho(request)
        carrinho.add(product_id, quantity, True)

    return redirect('carrinho_view')       

def remove_from_carrinho(request, product_id):
    carrinho = Carrinho(request)
    carrinho.remove(product_id)

    return redirect('carrinho_view')

def carrinho_view(request):
    carrinho = Carrinho(request)

    return render(request, 'loja/carrinho_view.html', {'carrinho': carrinho})

@login_required
def checar_comprar(request):
    carrinho = Carrinho(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():

            total_price = 0
            for item in carrinho:
                product = item['product']
                total_price += product.price * int(item['quantity'])

            order = form.save(commit=False)
            order.criado_por = request.user
            order.valor_pago = total_price
            order.save()

            for item in carrinho:
                product = item['product']
                quantity = int(item['quantity'])
                price = product.price * quantity

                item = OrderItem.objects.create(order=order, product=product, price=price, quantity=quantity)

            carrinho.clear()

            return redirect('minhaconta')
            
    else:
        form = OrderForm()

    return render(request, 'loja/checar_comprar.html', {'carrinho': carrinho, 'form': form})

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
