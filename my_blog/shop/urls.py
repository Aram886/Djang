from django.contrib import admin
from django.urls import path
from shop.views import *

urlpatterns = [
    path('', index),
    path('products.html', product),
    path('news.html', news),
    path('about.html', full_news),
    path('contact.html', contact),
    path('search.html', search)
]

