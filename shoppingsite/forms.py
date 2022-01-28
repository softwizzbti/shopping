from django import forms
from shoppingsite.models import contact,faqs,comment,review,products,subscribe
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your models here.
class contactform(forms.ModelForm):
	message=forms.CharField(max_length=500)
	name=forms.CharField(max_length=100)
	email=forms.CharField(max_length=100)
	sub=forms.CharField(max_length=100)
	class Meta:
		model=contact
		fields='__all__'
		

class faqsform(forms.ModelForm):
	question=forms.CharField(max_length=500)
	answer=forms.CharField(max_length=1000)
	class Meta:
		model=faqs
		fields='__all__'
		

class commentform(forms.ModelForm):
	name=forms.CharField(max_length=200)
	email=forms.CharField(max_length=100)
	phone=forms.CharField(max_length=200)
	comment=forms.CharField(max_length=1000)
	userid=forms.ModelChoiceField(queryset=User.objects.all())
	productid=forms.ModelChoiceField(queryset=products.objects.all())
	class Meta:
		model=comment
		fields='__all__'
		
class reviewform(forms.ModelForm):
	name=forms.CharField(max_length=200)
	email=forms.CharField(max_length=100)
	phone=forms.CharField(max_length=200)
	message=forms.CharField(max_length=1000)
	userid=forms.ModelChoiceField(queryset=User.objects.all())
	pid=forms.ModelChoiceField(queryset=products.objects.all())
	class Meta:
		model=review
		fields='__all__'
		
class signform(UserCreationForm):
	class Meta:
		model=User
		fields=('first_name','email','username','password1','password2',)
		
class subscribeform(forms.ModelForm):
	email=forms.CharField(max_length=500)
	class Meta:
		model=subscribe
		fields='__all__'
		
