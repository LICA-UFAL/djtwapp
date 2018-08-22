from django.db import models

BOT_EXPLICATIONS = [
    "È bot por causa da quantidade de posts",
    "È bot por causa do blablabla",
    "È bot por causa do blablabla2",
]

class Question(models.Model):
    text = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

twitter_accounts_attrs = {
    'name': models.CharField(max_length=32),
    'id' : models.IntegerField(primary_key=True, unique=True),
    'name' : models.CharField(max_length=255),
    'total_votes' : models.IntegerField(default=0),
    'bot_votes' : models.IntegerField(default=0),
    '__module__': 'profiles.models'
}


for cont in range(len(BOT_EXPLICATIONS)):
    twitter_accounts_attrs["answer_{0}_votes".format(cont+1)]= models.IntegerField(default=0)

Twitter_accounts = type("Twitter_accounts", (models.Model,), twitter_accounts_attrs)