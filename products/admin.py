from django.contrib import admin

# Register your models here.
from django.contrib import admin
from products.models import Product_item, Book

admin.site.register(Product_item)

admin.site.register(Book)