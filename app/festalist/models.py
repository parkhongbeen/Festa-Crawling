# Create your models here.
from django.db import models

# Create your models here.
from members.models import User


class FestaList(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=True)
    image = models.CharField(max_length=150, blank=True)
    host = models.CharField(max_length=150, blank=True)
    date = models.CharField(max_length=150, blank=True)
    content = models.TextField(blank=True)
    apply = models.CharField(max_length=150, blank=True)
    tickets = models.CharField(max_length=300, blank=True)
    link = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date', 'id']
        indexes = [
            models.Index(fields=['date', 'id'])
        ]

class FestaListKeyword(models.Model):
    keyword = models.CharField(max_length=150, blank=True)
    user = models.ManyToManyField(User, null=True)

    def __str__(self):
        return self.keyword
