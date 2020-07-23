from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact
from math import ceil

def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))

    allProds = []
    catprods = Product.objects.values('category', 'id')
    categories = {item['category'] for item in catprods} #assigns category of items in catprods to cats
    # a list of category is made
    for category in categories:
        prod = Product.objects.filter(category=category) 
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(nSlides), nSlides])

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)

def about (request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phoneNumber = request.POST.get('phoneNumber', '')
        description = request.POST.get('description', '')
        print(name, email, phoneNumber, description)
        contact_details = Contact(name = name, email = email, phoneNumber = phoneNumber, description = description)
        contact_details.save()
    return render(request, 'shop/contact.html')


def tracker(request):
    return HttpResponse('Inside Tracker')

def search(request):
    return HttpResponse('Inside Search')

def productView(request, myid):
    product = Product.objects.filter(id =myid) 
    print(product)
    return render(request, 'shop/productview.html', {'product': product[0]})

def checkout(request):
    return HttpResponse('Inside Checkout')