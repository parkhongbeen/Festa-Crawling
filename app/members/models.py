from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name = models.CharField('이름', max_length=50, null=True)
    email = models.EmailField('이메일', unique=True)
    username = models.CharField('아이디', max_length=50, null=True)

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []

    # objects = CustomUserManager()

    def __str__(self):
        return self.email
