from django import forms



class subscription_form(forms.Form):

    subscription = [
    ('Monthly/User', 'User: Monthly Subscription $0.99'),
    ('Yearly/User', 'User: Yearly Subscription $9.99'),
    ('Monthly/Advertising', 'To Advertise: Monthly costs $29.99'),
    ('Yearly/Advertising', 'To Advertise: Yearly costs $229.99'),
]


    right_package = forms.ChoiceField(label='Choose Your Subscription/Package', choices=subscription, required=False)