from django import forms
from blogapp.models import Product
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

#Django form
class EmpForm(forms.Form):
    empname=forms.CharField(max_length=50)
    mobile=forms.IntegerField()
    department=forms.CharField(max_length=50)
    date_of_joining=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))


#Model form
class ProductForm(forms.ModelForm):
    name=forms.CharField(max_length=50)
    category=forms.CharField(max_length=50)
    price=forms.CharField()
    Status=forms.CharField(max_length=50)
      
    '''class Meta:
       model=Product
       fields=['name','category','price','Status']'''

#Model form for user registration
class UserRegister(UserCreationForm):
    class Meta:
        model=User

        fields=['username','first_name','last_name','email']