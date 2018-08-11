from django.shortcuts import render
from .forms import UserForm

# Create your views here.
def index(request):
	return render(request,"index.html")

def cadastro(request):
    if(request.method=="POST"):
        pass
    else:
        pass
    return render(request,"cadastro_usuario.html",{"form":UserForm()})