from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.conf import settings

from accounts.forms import LoginForm

# Create your views here.
def index(request):
    return render(request, "profiles/pages/index.html", {"form": LoginForm()})