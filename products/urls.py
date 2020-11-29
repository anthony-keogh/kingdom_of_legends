from products.views import product_page, all_Stories
from django.contrib import admin
from django.urls import include, re_path
from django.urls import path

urlpatterns = [
    path('', product_page, name='products'),
    #path('product', product, name="product"),
    path('all_stories', all_Stories, name='all_Stories'),
]