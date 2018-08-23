from random import choice

from django.db import models


class Twitter_account(models.Model):
    name = models.CharField(max_length=255)
    id = models.IntegerField(primary_key=True, unique=True)
    total_votes = models.IntegerField(default=0)
    bot_votes = models.IntegerField(default=0)
    image_url = models.CharField(max_length=255)

    answer_1_votes = models.IntegerField(default=0)
    answer_2_votes = models.IntegerField(default=0)
    answer_3_votes = models.IntegerField(default=0)
    answer_4_votes = models.IntegerField(default=0)
    answer_5_votes = models.IntegerField(default=0)

    def vote(self, user, is_bot=False, answers=None):
        user.vote_count += 1
        self.total_votes += 1
        if(is_bot):
            self.bot_votes += 1
            for answer in answers:
                ans_str = "answer_{0}_votes".format(answer)
                ans_count = self.__getattribute__(ans_str)
                self.__setatt__(ans_str, ans_count+1)
        user.save()



    @classmethod
    def get_random_account(cls):
        return choice(cls.objects.all())
