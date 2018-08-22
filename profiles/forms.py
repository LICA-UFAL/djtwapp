from django import forms
from .models import BOT_EXPLICATIONS


def get_bot_explications():
    return [(str(count), explication) for count, explication in enumerate(BOT_EXPLICATIONS)]


class BotExplicationForm:
    choices = forms.ChoiceField(choices=get_bot_explications())

