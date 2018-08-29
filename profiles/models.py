from random import choice

from django.db import models


class Twitter_account(models.Model):
    name = models.CharField(max_length=255)
    screen_name = models.CharField(max_length=255, default="default")
    id = models.IntegerField(primary_key=True, unique=True)
    total_votes = models.IntegerField(default=0)
    bot_votes = models.IntegerField(default=0)
    image_url = models.CharField(max_length=255)

    answer_1_votes = models.IntegerField(default=0)
    answer_2_votes = models.IntegerField(default=0)
    answer_3_votes = models.IntegerField(default=0)
    answer_4_votes = models.IntegerField(default=0)
    answer_5_votes = models.IntegerField(default=0)

    def __str__(self):
        return self.screen_name

    @classmethod
    def get_random_account(cls):
        return choice(cls.objects.filter(total_votes__lte=20))
