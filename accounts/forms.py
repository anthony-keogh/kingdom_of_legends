from django import forms

from django.core.exceptions import ValidationError

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User





class UserLoginForm(forms.Form):
    email_or_username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(),  min_length= 6, max_length= 20, required=True )
    email = forms.CharField(label="Email", widget=forms.EmailInput(), required=True)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label="Confirmation of password", widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ['username',
                  'email',
                  'password1',
                  'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email address must be unique')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords are not a match")
        return password2