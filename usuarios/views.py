from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.urls import reverse

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
            
        
        
        user = User.objects.filter(username=username)
        if user.exists():
            messages.add_message(request, constants.ERROR, 'Nome de usuário já cadastrado')
            return redirect(reverse(cadastro))

        user = User.objects.create_user(username=username, email=email, password=senha)

        return redirect(reverse(login))