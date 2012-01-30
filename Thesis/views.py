from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

def start(request):
	if request.user.is_authenticated():
	    # TODO: show profile
		return render_to_response('pageTemplates/profile.html', {'pages': ['Play', 'Discover', 'Help a Puzzlaefer'], 'current_page': 'Play' })
	else:
	    return HttpResponseRedirect('/accounts/login/')
    