from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser

class SignupForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model=CustomUser
        fields=['first_name', 'last_name','profile_picture','username','email','password','confirm_password',
                'role','address_line1','city','state','pincode']
    def clean(self):
        cleaned_data=super().clean()
        if cleaned_data.get("password")!=cleaned_data.get("confirm_password"):
            self.add_error("Confirm_password"," passwrod are does not match")
        return cleaned_data
class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={"autofocus":True}))
    password=forms.CharField(widget=forms.PasswordInput)
    