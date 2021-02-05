from django.shortcuts import render

# Create your views here.

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from accounts.views import login
from django.contrib.auth.models import User
from products.models import Product_item, Book
from products.forms import subscription_form
from django.views import generic
##https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Generic_views

def book_list(request):
    book_list = Book.objects.all()
    return render(request, 'book_list.html', {'book_list': book_list})

def book_detail_view(request, pk):
    book = Book.objects.get(pk=pk)

    return render(request, 'book.html', {'book': book})


def all_Stories(request):
  #  products = Product_item.objects.all()
    return render(request, 'all_stories.html')
    #return render(request, 'product.html', {'products':products})





@login_required(login_url='login')
def product_page(request):
    products = Product_item.objects.all()
    if request.method=='POST':
        packageform = subscription_form(request.POST)

        if packageform.is_valid():

            packageform.save()

            return redirect('purchase_product.html')
            
            
 
    else:
        packageform = subscription_form()
        
    return render(request, "product.html",{'packageform':packageform,'products':products})