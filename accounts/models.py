from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password

from profiles.models import Twitter_account

from firebase_admin import db

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, username, password, email=None, is_active=True, is_staff=False, is_admin=False):
        if not username:
            raise ValueError("Usuário deve ter um nome")
        if not password:
            raise ValueError("Usuário deve ter uma senha")

        user_obj = self.model(username=username)
        if(email != None):
            user_obj.email = email

        user_obj.set_password(password)

        user_obj.staff = is_staff
        user_obj.active = is_active
        user_obj.admin = is_admin

        user_obj.save(using=self._db)

        return user_obj

    def create_superuser(self, username, password, email=None):
        user = self.create_user(username, password, email,
                                is_staff=True, is_admin=True)

        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True, verbose_name="Nome de usuário")
    email = models.EmailField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    vote_count = models.IntegerField(default=0)
    vote_account = models.ForeignKey(Twitter_account, on_delete=models.SET_NULL, blank=True, null=True)

    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def vote(self, is_bot=False, answers=None):
        self.vote_count += 1
        self.vote_account.total_votes += 1
        if(is_bot):
            self.vote_account.bot_votes += 1
            for answer in answers:
                ans_str = "answer_{0}_votes".format(answer)
                ans_count = self.vote_account.__getattribute__(ans_str)
                self.vote_account.__setattr__(ans_str, ans_count+1)
        if(self.admin or self.staff or self.vote_account.total_votes >= 20):
            self.vote_account.classified = True
        self.vote_account.save()
        self.save_vote(self.username, self.vote_account.screen_name, is_bot)
        self.set_vote_account()

    def save_vote(self, username, screen_name, is_bot):
        root = db.reference('/votos')
        new_user = root.child(username).update({
            screen_name: is_bot,
        })

    def get_vote_accounts(self):
        root = db.reference('/votos')
        accounts = root.child(self.username).get()
        if(accounts != None):
            return accounts.keys()
        else:
            return []

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def set_vote_account(self):
        self.vote_account = Twitter_account.get_random_account(user=self)
        self.save()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_active(self):
        return self.active

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @classmethod
    def save_instance(cls, user):
        cls.objects.create_user(user.username,user.password)

    @classmethod
    def get_user_by_name(cls,username):
        return cls.objects.filter(username=username)[0]

