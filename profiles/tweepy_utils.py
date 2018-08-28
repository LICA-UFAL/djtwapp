from django.settings import TWEEPY_API


def cad_dataset(Model,screen_names):
    """
    Salva uma lista de contas do twitter no banco de dados.
    Para isso é necessario acessar o shell do django usando
    python manage.py shell, depois importar o modelo Twitter_account
    fazendo from profiles.models import Twitter_account, e importar essa 
    funcão usando from profiles.tweepy_utils import cad_dataset, desse forma é 
    só chamar a função cad_dataset(Twitter_account,<lista de screen_names dos usuários>)
    """
    for screen_name in screen_names:
        user = TWEEPY_API.get_user(screen_name=screen_name)
        Model(name=user.name, id=user.id, image_url=user.profile_image_url_https).save()