from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Order, OrderItem
from django.db.models import Q
from .carrinho import Carrinho
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
from django.conf import settings
import json
import stripe
from django.http import JsonResponse

def add_to_carrinho(request, product_id):
    carrinho = Carrinho(request)
    carrinho.add(product_id)

    return redirect('carrinho_view')

def success(request):
    return render(request, 'loja/success.html')

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
    if carrinho.get_total_custo == 0:
        return redirect('carrinho_view')
    
    if request.method == 'POST':
        data = json.loads(request.body)

        p_name = data['p_name']
        s_name = data['s_name']
        address = data['address']
        zip_numero = data['zip_numero']
        city = data['city']

        if p_name and s_name and address and zip_numero and city:

            form = OrderForm(request.POST)
            
            total_price = 0
            items = []
            for item in carrinho:
                product = item['product']
                total_price += product.price * int(item['quantity'])
                items.append({
                    'price_data':{
                        'currency': 'usd',
                        'product_data':{
                            'nome': product.title,
                        },
                        'unit_amount': product.price
                    },
                        'quantity': item['quantity']
                })

            stripe.api_key = settings.STRIPE_SECRET_KEY
            session = stripe.checkout.Session.create(
                payment_method_types = ['card'],
                line_items = items,
                mode = 'payment',
                success_url = 'http://127.0.0.1:8000/cart/sucess',
                cancel_url = 'http://127.0.0.1:8000/cart/'
            )   

            payment_intent = session.payment_intent

            order = Order.objects.create(
                p_name = p_name,
                s_name = s_name,
                address = address,
                zip_numero = zip_numero,
                city = city,

                criado_por = request.user,
                esta_pago = True,
                payment_intent = payment_intent,
                valor_pago = total_price
            )

            for item in carrinho:
                product = item['product']
                quantity = int(item['quantity'])
                price = product.price * quantity

                item = OrderItem.objects.create(order=order, product=product, price=price, quantity=quantity)

            carrinho.clear()

            return JsonResponse({'session': session, 'order': payment_intent})
            
    else:
        form = OrderForm()

    return render(request, 'loja/checar_comprar.html', {'carrinho': carrinho, 'form': form, 'pub_key': settings.STRIPE_PUB_KEY,})

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
