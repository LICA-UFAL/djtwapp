from django.urls import path

from .views import index, contato, guia

urlpatterns = [
    path("", index, name="profile_index"),
    path("contato/", contato, name="contato"),
    path("guia/", guia, name="guia")
]
