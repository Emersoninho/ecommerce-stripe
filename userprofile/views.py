from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import UserFrofile
from django.contrib.auth.decorators import login_required
from loja.forms import ProductForm
from loja.models import Product, Order, OrderItem
from django.utils.text import slugify
from loja.models import Product
from django.contrib import messages
from django.shortcuts import get_object_or_404

def vendor_details(request, pk):
    user = User.objects.get(pk=pk)
    products = user.products.filter(status=Product.ATIVAR)

    return render(request, 'userprofile/vendor_details.html', {'user': user, 'products': products})

@login_required
def minha_loja(request):
    products = request.user.products.exclude(status=Product.DELETADO)
    order_items = OrderItem.objects.filter(product__user=request.user)
    
    return render(request, 'userprofile/minhaloja.html', {'products': products, 'order_items': order_items})

@login_required
def minha_loja_pedido_detalhes(request, pk):
    order = get_object_or_404(Order, pk=pk)
    
    return render(request, 'userprofile/minha_loja_pedido_detalhes.html', {'order': order})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            title = request.POST.get('title')
            product = form.save(commit=False)
            product.user = request.user
            product.slug = slugify(title)
            product.save()

            messages.success(request, 'ESTE PRODUTO FOI CADASTRADO COM SUCESSO!')

            return redirect('loja')
    else:
        form = ProductForm()
    return render(request, 'userprofile/product_form.html', {'title': 'Adicionar Produto', 'form': form})

@login_required
def edit_product(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()

            messages.success(request, 'ESTE PRODUTO FOI EDITADO COM SUCESSO!')

            return redirect('loja')
    else:    
        form = ProductForm(instance=product)
    return render(request, 'userprofile/product_form.html',
                  {'title': 'Editar Produto',
                   'product': product,
                   'form': form
                   }) 

@login_required
def delete_product(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)
    product.status = Product.DELETADO
    product.save()
    
    messages.success(request, 'ESTE PRODUTO FOI DELETADO COM SUCESSO!')

    return redirect('loja')
    
@login_required
def minha_conta(request):
    return render(request, 'userprofile/minhaconta.html')

def cadastrar(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            userFrofile = UserFrofile.objects.create(user=user)

            return redirect('frontpage')
    else:
        form = UserCreationForm()

    return render(request, 'userprofile/cadastrar.html', {'form': form})    
    