# Create your models here.
from django.db import models

# Create your models here.
from members.models import User


class FestaList(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=True)
    organizer = models.CharField(max_length=150, blank=True)
    date = models.CharField(max_length=150, blank=True)
    price = models.CharField(max_length=150, blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.user, self.title, self.date
