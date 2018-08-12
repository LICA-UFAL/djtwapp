from django.shortcuts import render

from .forms import UserForm

# Create your views here.

def login(request):
	if(request.method=="POST"):
		userform = UserForm(request.POST)

	else:
		userform = UserForm()

	return render(request, "login", {"form":userform, "action_url":"/"})

def cadastro(request):
	if(request.method=="POST"):
		userform = UserForm(request.POST)
		if(userform.is_valid()):
			userform.save()

	else:
		userform=UserForm()

	return render(request, "cadastro.html", {"form":userform,"action_url":"/accounts/cadastro/"})


def logout(request):
	pass