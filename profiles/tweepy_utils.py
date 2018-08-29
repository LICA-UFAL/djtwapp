import time

from djtwapp.settings import TWEEPY_API, RATE_LIMIT_ERROR, TWEEP_ERROR
from profiles.models import Twitter_account

def is_valid_account(user):
    if(user.statuses_count >= 200 and user.lang == 'pt'):
        return True
    return False

def cad_dataset(screen_names):
    """
    Salva uma lista de contas do twitter no banco de dados.
    Para isso é necessario acessar o shell do django usando
    python manage.py shell, depois importar o modelo Twitter_account
    fazendo from profiles.models import Twitter_account, e importar essa 
    funcão usando from profiles.tweepy_utils import cad_dataset, desse forma é 
    só chamar a função cad_dataset(Twitter_account,<lista de screen_names dos usuários>)
    """

    api = TWEEPY_API

    for screen_name in screen_names:
        try:
            user = api.get_user(screen_name=screen_name)
            if(is_valid_account(user)):
                account = Twitter_account(name=user.name, screen_name=screen_name, image_url=user.profile_image_url_https)
                account.save()
        except RATE_LIMIT_ERROR:
            print("Rate Limit")
            for i in range(15):
                time.sleep(60)
                print(str(15-(i+1)) + " minutes left")
        except TWEEP_ERROR as e:
            print(e)
        except Exception as e:
            print(e)