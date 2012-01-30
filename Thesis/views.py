from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from Thesis.forms import UserProfileForm

def start(request):
	if request.user.is_authenticated():
	    # TODO: show profile
		return render_to_response('pageTemplates/profile.html', RequestContext(request, {'pages': ['Play', 'Discover', 'Help a Puzzlaef'], 'current_page': 'Play' }))
	else:
	    return HttpResponseRedirect('/accounts/login/')

@login_required
def show_profile(request):
	context = RequestContext(request)
#	for key, value in extra_context.items():
#		context[key] = callable(value) and value() or value
	form = UserProfileForm(data=request.POST)
	return render_to_response('pageTemplates/profile.html', {'form': form})
