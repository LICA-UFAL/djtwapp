import tweepy

consumer_key = '6vWSFssZSZ6ca87IUeSkV1VR2'
consumer_secret = 'zftYif2YKWnkeJblQGqIMst5q50gZ1qusYubZ73Rstp6fkO0bT'

access_token = '3755330536-ME2ulUmQGAO7ZG2I9znrvQjQDsOlTEavpauCynN'
access_token_secret = 'LfptIr4rQa9qKB1Lt3j2FxtThKwIaePQopz1JqwXaQCyW'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


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
        user = api.get_user(screen_name=screen_name)
        Model(name=user.name, id=user.id, image_url=user.profile_image_url_https).save()



