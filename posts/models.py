import datetime
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone

class UserProfile(models.Model):
    user_auth = models.OneToOneField(User, primary_key=True)
    phone = models.CharField(max_length=20, verbose_name="Phone number", null=True, default=None, blank=True)
    date_born = models.DateField(verbose_name="Born Date", null=True, default=None, blank=True)
    last_connexion = models.DateTimeField(verbose_name="Date of last connexion", null=True, default=None, blank=True)

    def __str__(self):
        return self.user_auth.username

class Publisher(UserProfile):
    specialisation = models.CharField(max_length=50, verbose_name="Specialisation")


class Post(models.Model):
    publisher = models.ForeignKey(Publisher)
    name = models.CharField(max_length=200)
    link = models.URLField(max_length=200, null=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)
    votes = models.IntegerField(default=0)

    def was_published_recently(self):
        return self.date_pub >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'date_pub'
    was_published_recently.boolean = True
    was_published_recently.short_description = "Published recently?"

    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(Publisher)
    post = models.ForeignKey(Post)
    content = models.TextField(max_length=200)
    date_pub = models.DateTimeField(auto_now_add=True)

class Vote(models.Model):
    post = models.ForeignKey(Post)
    user = models.ForeignKey(Publisher)
    date_vote = models.DateTimeField(auto_now_add=True)




