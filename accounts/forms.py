from django import forms
from .models import User


class RegisterUserForm(forms.ModelForm):
    password = forms.CharField(label='Senha' ,widget=forms.PasswordInput,)
    confirm_password = forms.CharField(label='Confirmar senha', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "password")


class LoginForm(forms.Form):
    username = forms.CharField(label="Nome de usuário")
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
