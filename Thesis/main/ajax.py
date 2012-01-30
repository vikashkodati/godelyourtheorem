'''
Created on Jan 29, 2012

@author:  Wissam Jarjoui (wjarjoui@mit.edu)
'''
from Thesis.forms import UserProfileForm
from Thesis.main.models import UserProfile
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from django.core import serializers
from Thesis.views import PAGES, PAGES_LOCATIONS
from django.template.loader import render_to_string
import string


@dajaxice_register
def send_form(request, form):
	dajax = Dajax()
	print form
	form = UserProfileForm(form)
	print form
	if form.is_valid():
		user_profile = UserProfile.objects.get(user_id = request.user.id)
		user_profile.location = form.cleaned_data['location']
		user_profile.save();
		dajax.remove_css_class('#my_form input','error')
		dajax.alert("This form is_valid(), your name is: %s" % form.cleaned_data.get('first_name'))
	else:
		dajax.remove_css_class('#my_form input','error')
		for error in form.errors:
			dajax.add_css_class('#id_%s' % error,'error')
	return dajax.json()

@dajaxice_register
def changePage(request, newPage):
	if (newPage == PAGES[0]):
		template = PAGES_LOCATIONS[0]
	elif (newPage == PAGES[1]):
		template = PAGES_LOCATIONS[1]
	elif (newPage == PAGES[2]):
		template = PAGES_LOCATIONS[2]
	print "um"+template
	render = render_to_string(template, {})
	print render
	dajax = Dajax()
	dajax.assign('#page-container','innerHTML',render)
	return dajax.json()
