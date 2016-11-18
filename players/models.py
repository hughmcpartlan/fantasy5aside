from __future__ import unicode_literals

from django.db import models

# Create your models here.



class Defender(models.Model):
    class Meta:
        app_label = 'defenders'

    full_name = models.CharField(max_length=200)
    team_name = models.CharField(max_length=200)

class Midfielder(models.Model):
    class Meta:
            app_label = 'midfielders'

    full_name = models.CharField(max_length=200)
    team_name = models.CharField(max_length=200)

class Striker(models.Model):
    class Meta:
        app_label = 'strikers'

    full_name = models.CharField(max_length=200)
    team_name = models.CharField(max_length=200)

    def __str__(self):
        return self.full_name