'''
Created on Jan 29, 2012

@author:  Wissam Jarjoui (wjarjoui@mit.edu)
'''

from django import forms

class UserProfileForm(forms.form):
    location = forms.CharField(max_length = 100)
    avatar = forms.ImageField()