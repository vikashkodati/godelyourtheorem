from Thesis.activation import activate_user
from Thesis.forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import login, logout
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def register1(request):
    c = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/books/")
    else:
        form = UserCreationForm()
    return render_to_response("register/register.html", {
        'form': form,
    }, context_instance = c)

@csrf_protect
def register(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = RegisterForm()
    return render_to_response("register/register.html", {'form': form,  }, context_instance = c)

@csrf_protect
def activate(request):
    c = {}
    c.update(csrf(request))
    user = request.GET.get('user')
    code = request.GET.get('code')
 
    if activate_user(user,  code):
        return HttpResponseRedirect("/")
    else:
        raise Http404

@csrf_protect
def limited_login(request):
    return login(request)

@csrf_protect
def limited_logout(request):
    return logout(request)