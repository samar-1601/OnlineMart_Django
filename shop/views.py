from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides':nSlides, 'range': range(nSlides), 'product': products}
    return render(request, 'shop/index.html', params)

def about (request):
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse('Inside Contacts')

def tracker(request):
    return HttpResponse('Inside Tracker')

def search(request):
    return HttpResponse('Inside Search')

def productView(request):
    return HttpResponse('Inside ProductView')

def checkout(request):
    return HttpResponse('Inside Checkout')