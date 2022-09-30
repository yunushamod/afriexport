from django.contrib.auth.models import User
from django import forms
from .models import Profile


class UserRegistrationForm(forms.ModelForm):
    BUSINESS_TYPES = (
        ('BY', 'Buyer'),
        ('SL', "Seller"), ('FR', 'Freight Forwarder')
    )
    company_name = forms.CharField(max_length=250, required=True)
    password = forms.CharField(label = 'Password',widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, required=True)
    phone = forms.CharField(label='Phone', max_length=11, required=True)
    business_type = forms.ChoiceField(choices = BUSINESS_TYPES, label='Business Type')
    address = forms.CharField(max_length=350, required=True)
    photo = forms.ImageField(required=False)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email',]
    
    def clean_confirm_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['confirm_password']:
            raise forms.ValidationError("Passwords do not match")
        return cd['confirm_password']
    def clean_email(self):
        cd = self.cleaned_data['email']
        if User.objects.filter(email=cd).exists():
            raise  forms.ValidationError("Email has already been used")
        return cd

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def clean_email(self):
        data = self.cleaned_data['email']
        qs = User.objects.exclude(id=self.instance.id).filter(email=data)
        if qs.exists():
            raise forms.ValidationError('Email already in use.')
        return data

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'company_name', 'address', 'photo']
