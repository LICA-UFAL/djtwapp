import tweepy

from models import Twitter_account

consumer_key = '6vWSFssZSZ6ca87IUeSkV1VR2'
consumer_secret = 'zftYif2YKWnkeJblQGqIMst5q50gZ1qusYubZ73Rstp6fkO0bT'

access_token = '3755330536-ME2ulUmQGAO7ZG2I9znrvQjQDsOlTEavpauCynN'
access_token_secret = 'LfptIr4rQa9qKB1Lt3j2FxtThKwIaePQopz1JqwXaQCyW'

auth = tweepy.OAuthHandler(consume_key, consumer_secret)
auth.access_token_secret(access_token, access_token_secret)

api = API(auth)

user = api.get_user(screen_name="PaiNGamingBR")

account = Twitter_account(name=user.name, id=user.id, image_url=user.profile_image_url_https)
account.save()