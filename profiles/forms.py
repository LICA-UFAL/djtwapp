from django import forms

BOT_EXPLICATIONS = [
    "Comportamento repetitivo",
    "Posta em intervalos muito curto",
    "Usa a conta apenas para fazer propaganda",
    "É bot de uma empresa conhecida",
    "É bot por conta das hashtags"
]

error_messages = {
    'NotSelectedChoice': 'Porfavor selecionar uma opção'
}

def get_bot_explications():
    return [(str(count+1), explication) for count, explication in enumerate(BOT_EXPLICATIONS)]


class BotExplicationForm(forms.Form):
    choices = forms.ChoiceField(choices=get_bot_explications(), widget=forms.CheckboxSelectMultiple)

    def clean_choices(self):
        choices = self.cleaned_data["choices"]

        if(len(choices) == 0):
            raise forms.ValidationError(error_messages['NotSelectedChoice'], code='NotSelectedChoice')
        else:
            return choices


    def get_answers(self):
        choices = self.cleaned_data["choices"]
        print(choices)

        return choices
