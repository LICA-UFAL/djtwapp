from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.conf import settings

from accounts.forms import LoginForm

# Create your views here.
def index(request):
    # Log-in form
    if(request.method == "POST"):
        form = LoginForm(request.POST)

        if(form.is_valid()):
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(
                request, username=username, password=password)
            
            if(user is not None):
                auth.login(request, user)
                return redirect(settings.LOGIN_REDIRECT_URL)
            else:
                return redirect('/accounts/login/')
    else:
        form = LoginForm()
    return render(request, "profiles/index.html", {'form': form, "action_url": "/accounts/login/"})