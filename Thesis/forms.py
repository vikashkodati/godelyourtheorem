'''
Created on Jan 29, 2012

@author:  Wissam Jarjoui (wjarjoui@mit.edu)
'''
from django import forms

attrs_dict = {'class': 'required'}

class UserProfileForm(forms.Form):
    first_name = forms.CharField(required=False, widget=forms.TextInput(), max_length = 30)
    last_name = forms.CharField(required=False, widget=forms.TextInput(), max_length = 30)
    avatar = forms.ImageField(required=False)
    location = forms.CharField(widget=forms.TextInput(), max_length = 100)