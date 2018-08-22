from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
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
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

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
