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
    """
    Returns
    --------
    A list of tuples with pairs of number and justifications
    """
    return [(str(count+1), explication) for count, explication in enumerate(BOT_EXPLICATIONS)]


class BotExplicationForm(forms.Form):
    reasons = forms.MultipleChoiceField(choices=get_bot_explications(), required=False, label="É bot por conta",
                                         widget=forms.CheckboxSelectMultiple)
    
    def clean_reasons(self):
        reasons = self.cleaned_data["reasons"]
        if(len(self.cleaned_data["reasons"]) == 0):
            self.is_bot = False
        else:
            self.is_bot = True

        
        return reasons


    def get_reasons(self):
        return self.cleaned_data["reasons"]