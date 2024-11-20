from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import UserFrofile
from django.contrib.auth.decorators import login_required
from loja.forms import ProductForm
from loja.models import Product, Category
from django.utils.text import slugify

def vendor_details(request, pk):
    user = User.objects.get(pk=pk)
    return render(request, 'userprofile/vendor_details.html', {'user': user})

@login_required
def minha_loja(request):
    return render(request, 'userprofile/minhaloja.html')

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

            return redirect('loja')
    else:
        form = ProductForm()
        return render(request, 'userprofile/add_product.html', {'form': form})

    form = ProductForm()
    return render(request, 'userprofile/add_product.html', {'form': form})

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
    