'''
Created on Jan 29, 2012

@author:  Wissam Jarjoui (wjarjoui@mit.edu)
'''
from Thesis.forms import UserProfileForm
from Thesis.main.models import UserProfile
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register


@dajaxice_register
def send_form(request, form):
    dajax = Dajax()
    form = UserProfileForm(form)
    
    if form.is_valid():
        user_profile = UserProfile.objects.get(user_id = request.user.id)
        print user_profile
        user_profile.location = form.cleaned_data['location']
        user_profile.save();
        dajax.remove_css_class('#my_form input','error')
        dajax.alert("This form is_valid(), your name is: %s" % form.cleaned_data.get('first_name'))
    else:
        dajax.remove_css_class('#my_form input','error')
        for error in form.errors:
            dajax.add_css_class('#id_%s' % error,'error')
    return dajax.json()