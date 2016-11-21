from __future__ import unicode_literals

from django.db import models

# Create your models here.
from players.models import Defender, Midfielder, Striker

class Team(models.Model):
    owner = models.ForeignKey('accounts.User', related_name='teams_owned')
    name = models.CharField(max_length=30)
    total_points = models.IntegerField(default=0)
    gameweek_points = models.IntegerField(default=0)
    defender = models.ForeignKey(Defender, related_name='as_defender')
    midfielder1 = models.ForeignKey(Midfielder, related_name='as_midfielder1')
    midfielder2 = models.ForeignKey(Midfielder, related_name='as_midfielder2')
    striker1 = models.ForeignKey(Striker, related_name='as_striker1')
    striker2 = models.ForeignKey(Striker, related_name='as_striker2')

    def __str__(self):
        return self.name





