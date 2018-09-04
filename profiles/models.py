from random import choice

from django.db import models


class Twitter_account(models.Model):
    name = models.CharField(max_length=255)
    screen_name = models.CharField(max_length=255, default="default")
    id = models.IntegerField(primary_key=True, unique=True)
    total_votes = models.IntegerField(default=0)
    bot_votes = models.IntegerField(default=0)
    image_url = models.CharField(max_length=255)
    classified = models.BooleanField(default=False)
    
    answer_1_votes = models.IntegerField(default=0)
    answer_2_votes = models.IntegerField(default=0)
    answer_3_votes = models.IntegerField(default=0)
    answer_4_votes = models.IntegerField(default=0)
    answer_5_votes = models.IntegerField(default=0)

    def __str__(self):
        return self.screen_name

    def reset_values(self):
        self.total_votes = 0
        self.bot_votes = 0
        self.classified = False

    @classmethod
    def get_random_account(cls, user):
        if(user.is_admin or user.is_staff):
            return choice(cls.objects.filter(total_votes=0, classified=False))
        return choice(cls.objects.filter(classified=False))
