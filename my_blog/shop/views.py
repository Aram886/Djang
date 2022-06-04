from urllib import request
from django.shortcuts import render

def index(request):
    return render(request, 'shop/index.html')

def product(request):
    return render(request, 'shop/product.html')

def news(request):
    return render(request, 'shop/news.html')

def full_news(request):
    return render(request, 'shop/full_news.html')

def contact(request):
    return render(request, 'shop/contact.html')

def search(request):
    return render(request, 'shop/search.html')