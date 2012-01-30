from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from Thesis.forms import UserProfileForm

PAGES = ['Play', 'Discover', 'Help a Puzzlaef']
PAGES_LOCATIONS = ['pageTemplates/play.html', 'pageTemplates/discover.html', 'pageTemplates/helpPuzzlaef.html']

def start(request):
	if request.user.is_authenticated():
	    # TODO: show profile
		form = UserProfileForm(data=request.POST)
		return render_to_response('pageTemplates/profile.html', RequestContext(request, {'form': form, 'pages': PAGES, 'current_page': 'Play' }))
	else:
	    return HttpResponseRedirect('/accounts/login/')

@login_required
def show_profile(request):
	context = RequestContext(request)
#	for key, value in extra_context.items():
#		context[key] = callable(value) and value() or value
	form = UserProfileForm(data=request.POST)
	return render_to_response('pageTemplates/profile.html', RequestContext(request, {'form': form, 'pages': PAGES, 'current_page': 'Play' }))

