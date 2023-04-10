from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.urls import reverse
from django.contrib import auth

# Create your views here.
def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirm_senha = request.POST.get('confirmar_senha')
        
        if not senha == confirm_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não são iguais')
            return redirect(reverse(cadastro))
            
        
        
        # Adicionar verificação de senha
        
        user = User.objects.filter(username=username)
        if user.exists():
            messages.add_message(request, constants.ERROR, 'Nome de usuário já cadastrado')
            return redirect(reverse(cadastro))

        user = User.objects.create_user(username=username, email=email, password=senha)

        return redirect(reverse(login))
    
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        #Apenas verifica se o usuario existe
        user = auth.authenticate(username=username, password=senha)
        
        if not user:
            messages.add_message(request, constants.ERROR, 'Username ou senha inválido.')
            return redirect(reverse(login))
        
        auth.login(request, user)
        return redirect('/eventos/novo_evento')