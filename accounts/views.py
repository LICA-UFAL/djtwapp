from django.shortcuts import render, redirect
from django.contrib import auth
from django.conf import settings

from .forms import RegisterUserForm, LoginForm
from .models import User

# Create your views here.


def login(request):
    if(request.method == "POST"):
        loginform = LoginForm(request.POST)

        if(loginform.is_valid()):
            username = loginform.cleaned_data.get("username")
            password = loginform.cleaned_data.get("password")
            user = auth.authenticate(
                request, username=username, password=password)

            if(user is not None):
                auth.login(request, user)

                return redirect(settings.LOGIN_REDIRECT_URL)
            else:
                print("error")

    else:
        userform = LoginForm()

    return render(request, "accounts/login.html", {"form": LoginForm, "action_url": "/accounts/login/"})


def cadastro(request):
    if(request.method == "POST"):
        register_user_form = RegisterUserForm(request.POST)

        if(register_user_form.is_valid()):
            user = register_user_form.save(commit=False)

            User.save_instance(user)

            return redirect(settings.REGISTER_REDIRECT_URL)

    else:
        register_user_form = RegisterUserForm()
    userform = RegisterUserForm()
    return render(request, "accounts/cadastro.html", {"form": register_user_form, "action_url": "/accounts/cadastro/"})


def logout(request):
    auth.logout(request)

    return redirect(settings.LOGOUT_REDIRECT_URL)