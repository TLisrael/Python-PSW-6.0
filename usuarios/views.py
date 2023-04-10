from django.shortcuts import render
from django.http import HttpResponse, request

# Create your views here.
def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')