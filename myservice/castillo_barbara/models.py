from django.conf import settings
from django.db import models
from django.utils import timezone
from contrib.django.models import User


# Create your models here.
class Idea(models.Model):
    idea = models.CharField(max_length=140)
    creation_date = models.DateTimeField(auto_now_add=True)

class Pensamiento(models.Model):
    idea = models.CharField(max_length=140)
    creation_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    usuario = models.ForeignKey (User.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def publish(self):
        self.published_date = timezone.now()
        self.save()