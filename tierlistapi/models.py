from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Tierlist(models.Model):
    title = models.TextField()
    likes = models.IntegerField()
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey('Game', on_delete=models.CASCADE)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    twitterAccount = models.TextField(blank=True, null=True)
    contactInformation = models.TextField(blank=True, null=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Game(models.Model):
    name = models.TextField()
    platform = models.TextField()
    year = models.IntegerField()

class Character(models.Model):
    name = models.TextField()
    version = models.TextField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)