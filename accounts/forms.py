from django import forms
from .models import User

error_messages = {
    "Username_exist": "Nome de usuário já existe",
    "Passwords_mismatch" : "As senhas são diferentes"
}

class RegisterUserForm(forms.ModelForm):
    password = forms.CharField(label='Senha' ,widget=forms.PasswordInput,)
    confirm_password = forms.CharField(label='Confirmar senha', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "password")

    def clean_username(self):
        username = self.cleaned_data["username"]
        if self.instance.username == username:
            return username
        try:
            User._default_manager.get(username=username)

            raise forms.ValidationError(error_messages["Username_exist"],code="Username_exist")

        except User.DoesNotExist:
            return username
    
    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(error_messages["Passwords_mismatch"],code="Passwords_mismatch")



class LoginForm(forms.Form):
    username = forms.CharField(label="Nome de usuário")
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

    
