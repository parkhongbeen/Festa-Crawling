# Create your models here.
from django.db import models

# Create your models here.
from members.models import User


class FestaList(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=True)
    image = models.ImageField(blank=True)
    host = models.CharField(max_length=150, blank=True)
    date = models.CharField(max_length=150, blank=True)
    content = models.CharField(max_length=150, blank=True)
    apply = models.CharField(max_length=150, blank=True)
    tickets = models.CharField(max_length=150, blank=True)
