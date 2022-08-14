from django.db import models

class Rock(models.Model):

    name = models.CharField(max_length=40, default="Valentin")

    hunger_index    = models.IntegerField(max_length=100)
    health_index    = models.IntegerField(max_length=100)
    happiness_index = models.IntegerField(max_length=100)

    