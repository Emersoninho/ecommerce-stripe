from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import UserFrofile

def vendor_details(request, pk):
    user = User.objects.get(pk=pk)
    return render(request, 'userprofile/vendor_details.html', {'user': user})

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
    