from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

<<<<<<< HEAD
from django.http import HttpResponse

# Create your views here.

def index (request):
    return HttpResponse('Olá... seja bem vindo à enquete')

def sobre (request):
    return HttpResponse('Olá, este é um app de enquete')
=======


def index(request):
    return HttpResponse('Olá... seja bem vindo à enquete')
>>>>>>> ecd1c1aa8bde16f553ba2cabf0dbd9118c19ea56
