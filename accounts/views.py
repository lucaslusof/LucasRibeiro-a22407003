from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from .forms import RegistoForm

def login_view(request):
    erro = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            erro = 'Credenciais inválidas.'
    return render(request, 'accounts/login.html', {'erro': erro})

def logout_view(request):
    logout(request)
    return redirect('home')

def registo_view(request):
    form = RegistoForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        # adiciona automaticamente ao grupo autores
        grupo, _ = Group.objects.get_or_create(name='autores')
        user.groups.add(grupo)
        login(request, user)
        return redirect('home')
    return render(request, 'accounts/registo.html', {'form': form})
# Create your views here.
