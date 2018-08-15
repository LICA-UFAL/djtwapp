from django.db import models

BOT_EXPLICATIONS = [
    "È bot por causa da quantidade de posts",
    "È bot por causa do blablabla",
    "È bot por causa do blablabla2",
]
# Create your models here.
class Twitter_accounts(models.Model):

    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)
    total_votes = models.IntegerField(default=0)
    bot_votes = models.IntegerField(default=0)

    def __init__(self):
        models.Model.__init__(self)
        for count in range(len(BOT_EXPLICATIONS)):
            self.__setattr__("answer_{0}_votes".format(count), models.IntegerField(default=0))

    def __str__(self):
        return self.name

    @classmethod
    def add_more_accounts(cls):
        pass





