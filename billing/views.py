from django.shortcuts import render

# Create your views here.

# Create your views here.
from django.shortcuts import render, reverse
from django.conf import settings
import stripe
from .forms import amountForm, purchaseForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from accounts.views import login

##stripe.api_key = settings.STRIPE_SECRET

@login_required(login_url='login')
def purchase_product(request):
    if request.method=="POST":
        purchase_form = purchaseForm(request.POST)
        amount_form = amountForm(request.POST)
        
        if amount_form.is_valid() and purchase_form.is_valid():
            total_amount = amount_form.save(commit=False)
            user = request.user
            total_amount.user = user
            total_price = total_amount.price
            total_amount.save()
            
            try:
                customer = stripe.Charge.create(
                    amount=int(total_price * 100),
                    currency="EUR",
                    description=(
                        request.user.email +
                        " (" + request.user.username() + ")"),
                    source=token,
                    card = purchase_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
                
            if customer.paid:
                messages.error(request, "")
                return render(request, "Profile.html")
            else:
                messages.error(request, "Unable to take payment")
        
        else:
            print(purchase_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        purchase_form = purchaseForm()
        amount_form = amountForm
        
    return render(request, "purchase_product.html", {'amount_form': amount_form,'purchase_form': purchase_form})