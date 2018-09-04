from django import forms
from .models import User

error_messages = {
    "Username_dont_exist" : "Nome de usuário não existe",
    "Username_exist": "Nome de usuário já existe",
    "Password_invalid" : "Senha invalida",
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
            error=forms.ValidationError(error_messages["Passwords_mismatch"],code="Passwords_mismatch")
            self.add_error("confirm_password",error)


class LoginForm(forms.Form):
    username = forms.CharField(label="Nome de usuário")
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

    class Meta:
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username=username)

            return username

        except User.DoesNotExist:
            raise forms.ValidationError(error_messages["Username_dont_exist"],code="Username_dont_exist")

    def clean(self):
        cleaned_data = super().clean()

        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if "username" in cleaned_data:
            user = User.get_user_by_name(username)
            
            if(not user.check_password(password)):
                error=forms.ValidationError(error_messages["Password_invalid"],code="Password_invalid")
                self.add_error("password",error)
        
