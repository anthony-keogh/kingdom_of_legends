from django import forms
from .models import purchase_product

class purchaseForm(forms.Form):
    
    Year_Range = [(i, i) for i in range(2020, 2045)]
    Month_Range = [(i, i) for i in range(1,13)]
    
    
    stripe_id = forms.CharField(widget=forms.HiddenInput)
    credit_card_num = forms.CharField(label='Credit card number', required=False)
    expiry_year = forms.ChoiceField(label='Enter the Year', choices=Year_Range, required=False)
    expiry_month = forms.ChoiceField(label='Enter the  Month', choices=Month_Range, required=False)
    cvv = forms.CharField(label='Enter the Security code(CVV)', required=False)

class amountForm(forms.ModelForm):
    class Meta:
        model = purchase_product
        fields = ('price',)