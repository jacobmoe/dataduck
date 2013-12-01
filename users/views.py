from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.context_processors import csrf

def sign_in(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'users/sign_in.html', c)

def sign_up(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'users/sign_up.html', c)

def authenticate_user(request):
    # default to empty string, if nothing returned
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(
        username = username, 
        password = password
    )
   
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/tweets')
    else:
        return HttpResponseRedirect('/users/sign-up')

def create_user(request):
    username = request.POST.get('username', '')
    email = request.POST.get('email', '')
    password = request.POST.get('password', '')
    user = User.objects.create_user(
        username = username, 
        email = email, 
        password = password
    )
    return HttpResponseRedirect('/tweets')
