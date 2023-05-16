from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django.http import HttpResponse

# Create your views here.

def index (request):
    return HttpResponse('Olá... seja bem vindo à enquete')

def sobre (request):
    return HttpResponse('Olá, este é um app de enquete')