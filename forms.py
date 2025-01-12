from django import forms
from .models import *
from django.contrib.auth.models import User


class registerform(forms.ModelForm):
    class Meta:
        model=User
        fields=('first_name','email','username','password')
        widigets={
                
                'password':forms.PasswordInput()
                
        }
class registrationform(forms.ModelForm):
    class Meta:
        model=registrationmodel
        fields=('confirmpassword',)
        
class registerform1(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','password')
        widigets={
                
                'password':forms.PasswordInput()
                
        }

class predictForm(forms.Form):
    area= forms.CharField(max_length=1000)         

class spamForm(forms.Form):
    class Meta:
        model=spammodel
        fields=('category','domain','ip_address','server','malware','spamming','phishing','risk_score','suspicious','domain_rank')

class reportform(forms.ModelForm):
    class Meta:
        model=reportmodel
        fields=('sitename','reason')

class FeedForm(forms.ModelForm):
    class Meta:
        model=feedmodel
        fields=['email','feed']   