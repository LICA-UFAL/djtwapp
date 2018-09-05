from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.conf import settings

from accounts.forms import LoginForm

# Create your views here.
def index(request):
    if(request.method == 'POST'):
        user = request.user
        lista = [value for name,value in request.POST.items() if(name != "csrfmiddlewaretoken")]

        if(len(lista)==0):
            user.vote()
        else:
            user.vote(is_bot=True, answers=lista)

    return render(request, "profiles/pages/index.html", {"form": LoginForm()})

def contato(request):
    return render(request, "profiles/pages/contato.html", {})

def guia(request):
    return render(request, "profiles/pages/guia.html", {})