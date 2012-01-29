from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext


def start(request):
	if request.user.is_authenticated():
	    # TODO: show profile
		return HttpResponse("TODO: show profile")
	else:
	    return HttpResponseRedirect('/accounts/login/')
    