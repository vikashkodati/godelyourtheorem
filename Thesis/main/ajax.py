'''
Created on Jan 29, 2012

@author:  Wissam Jarjoui (wjarjoui@mit.edu)
'''
from Thesis.forms import UserProfileForm
from Thesis.main.models import UserProfile
from Thesis.main.utils import ResultUser
from Thesis.views import PAGES, PAGES_LOCATIONS
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from django.contrib.auth.models import User
from django.core import serializers
from django.template.loader import render_to_string
from django.utils import simplejson
import string


@dajaxice_register
def send_form(request, form):
    dajax = Dajax()
    form = UserProfileForm(form)
    if form.is_valid():
        user_profile = UserProfile.objects.get(user=request.user.id)
        user = User.objects.get(id = request.user.id)
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user_profile.avatar = form.cleaned_data['avatar']
        user_profile.location = form.cleaned_data['location']
        user.save()
        user_profile.save()
        dajax.remove_css_class('#my_form input', 'error')
        dajax.alert("This form is_valid(), your name is: %s" % form.cleaned_data.get('first_name'))
    else:
		dajax.remove_css_class('#my_form input', 'error')
		for error in form.errors:
			dajax.add_css_class('#id_%s' % error, 'error')
    return dajax.json()

@dajaxice_register
def changePage(request, newPage):
	if (newPage == PAGES[0]):
		template = PAGES_LOCATIONS[0]
	elif (newPage == PAGES[1]):
		template = PAGES_LOCATIONS[1]
	elif (newPage == PAGES[2]):
		template = PAGES_LOCATIONS[2]
	print "um" + template
	render = render_to_string(template, {})
	print render
	dajax = Dajax()
	dajax.assign('#page-container', 'innerHTML', render)
	return dajax.json()
    
@dajaxice_register
def find_locations(request, location):
	list = UserProfile.objects.filter(location__icontains = location)
	result = [ResultUser(x).__dict__ for x in list]
	return simplejson.dumps(result)