import time
import random

from djtwapp.settings import TWEEPY_API, RATE_LIMIT_ERROR, TWEEP_ERROR
from profiles.models import Twitter_account

api = TWEEPY_API

def original_user_image(user):
    image = user.profile_image_url_https
    return image.replace('_normal', '')

def is_valid_account(user):
    if(user.lang == 'pt' and not user.protected):
        return True
    return False

def cad_user(id):
    try:
        user = api.get_user(id = id)
        if(is_valid_account(user)):
            account = Twitter_account(name=user.name, screen_name=user.screen_name, image_url=original_user_image(user))
            account.save()
            return 1
        else:
            return 0
    except RATE_LIMIT_ERROR:
        print("Rate Limit")
        for i in range(15):
            time.sleep(60)
            print(str(15-(i+1)) + " minutes left")
        cad_user(screen_name)
    except TWEEP_ERROR as e:
        print(e)
    except Exception as e:
        print(e)

def cad_dataset(screen_names):
    """
    Salva uma lista de contas do twitter no banco de dados.
    Para isso é necessario acessar o shell do django usando
    python manage.py shell, depois importar o modelo Twitter_account
    fazendo from profiles.models import Twitter_account, e importar essa 
    funcão usando from profiles.tweepy_utils import cad_dataset, desse forma é 
    só chamar a função cad_dataset(Twitter_account,<lista de screen_names dos usuários>)
    """

    for screen_name in screen_names:
        cad_user(id = screen_name)

def save_parent(id, deep):
    if deep >= 0:
        deep -= 1
        followers_ids = api.followers_ids(id = id)
        if len(followers_ids) > 0:
            get_user_id = lambda followers_ids : followers_ids.pop(random.randrange(len(followers_ids)))
            user_id = get_user_id(followers_ids)
            while not cad_user(user_id) and len(followers_ids) > 0:
                user_id = get_user_id(followers_ids)

            save_parent(user_id, deep)

def remove_protected_account(account):
    try:
        _account = TWEEPY_API.get_user(screen_name=account.screen_name)
        if(_account.protected):
            print("conta {0} excluida".format(account.screen_name))
            account.delete()
    except RATE_LIMIT_ERROR:
        print("Rate Limit")
        for i in range(15):
            time.sleep(60)
            print(str(15-(i+1)) + " minutes left")
    except TWEEP_ERROR as e:
        print(e)
    except Exception as e:
        print(e)