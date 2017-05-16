# conding=utf-8
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def contacts(request):
    return render(request, 'contacts.html')

def product_list(request):
    return render(request, 'product_list.html')

def products(request):
    return render(request, 'products.html')