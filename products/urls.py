from products.views import product_page, all_Stories, book_list, book_detail_view
from django.contrib import admin
from django.urls import include, re_path
from django.urls import path

urlpatterns = [
    path('', product_page, name='products'),
    #path('product', product, name="product"),
    path('all_stories', all_Stories, name='all_Stories'),
    path('book_list', book_list, name='book_list'),
    path(r'^book/(?P<pk>/d+)/$', book_detail_view, name='book-detail-with-pk'),
    
]