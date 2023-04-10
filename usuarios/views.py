from django.shortcuts import render, redirect
from django.http import HttpResponse, request

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
            return redirect('/usuarios/cadastro')
    return HttpResponse('Teste')