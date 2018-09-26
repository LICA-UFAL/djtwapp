import time

from djtwapp.settings import TWEEPY_API, RATE_LIMIT_ERROR, TWEEP_ERROR
from profiles.models import Twitter_account

def original_user_image(user):
    image = user.profile_image_url_https
    return image.replace('_normal', '')

def is_valid_account(user):
    if(user.statuses_count >= 200 and user.lang == 'pt' and not user.protected):
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
                account = Twitter_account(name=user.name, screen_name=screen_name, image_url=original_user_image(user))
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