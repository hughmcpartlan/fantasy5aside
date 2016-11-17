from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Player(models.Model):
    class Meta:
        app_label = 'players'

    full_name = models.CharField(max_length=200)
    team_name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)


    def __str__(self):
        return self.full_name