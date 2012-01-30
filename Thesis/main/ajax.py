'''
Created on Jan 29, 2012

@author:  Wissam Jarjoui (wjarjoui@mit.edu)
'''
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register

from Thesis.forms import UserProfileForm

@dajaxice_register
def send_form(request, form):
    dajax = Dajax()
    form = UserProfileForm(form)

    if form.is_valid():
        
        dajax.remove_css_class('#my_form input','error')
        dajax.alert("This form is_valid(), your name is: %s" % form.cleaned_data.get('first_name'))
    else:
        dajax.remove_css_class('#my_form input','error')
        for error in form.errors:
            dajax.add_css_class('#id_%s' % error,'error')
    return dajax.json()

def changePage(request, newPage):
    dajax = Dajax()
  	print newPage
    return dajax.json()