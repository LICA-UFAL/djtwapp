from django.urls import path

from .views import cadastro,login,logout

urlpatterns =[
	path("cadastro/",cadastro,name="cadastro")
]

