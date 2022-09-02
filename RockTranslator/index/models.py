from email.policy import default
from xml.dom.minicompat import defproperty
from django.db import models
from django.contrib.postgres.fields import ArrayField


class Rock(models.Model):

    name = models.CharField(max_length=40, default="Valentin")

    hunger_index    = models.IntegerField()
    health_index    = models.IntegerField()
    happiness_index = models.IntegerField()

    image = models.ImageField(default="https://cdn.discordapp.com/attachments/432562983776944150/1009574236261720074/3.png", upload_to="rocks/")


class Massage(models.Model):
    autor   = models.CharField(max_length=40)
    context = models.TextField(max_length=2000)
    

class User(models.Model):

    name = models.CharField(max_length=20)
    curent_rock = models.IntegerField()

    available_rocks = ArrayField(models.IntegerField())

    exp = models.IntegerField(default=10)