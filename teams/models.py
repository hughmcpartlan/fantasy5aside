from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Team(models.Model):

    class Meta:
        app_label = 'teams'

    owner = models.ForeignKey('accounts.User', related_name='teams_owned')
    team_name = models.CharField(max_length=30)
    total_points = models.IntegerField()
    gameweek_points = models.IntegerField()
    defender = models.ForeignKey('players.Player', related_name='as_defender')
    midfielder1 = models.ForeignKey('players.Player', related_name='as_midfielder1')
    midfielder2 = models.ForeignKey('players.Player', related_name='as_midfielder2')
    striker1 = models.ForeignKey('players.Player', related_name='as_striker1')
    striker2 = models.ForeignKey('players.Player', related_name='as_striker2')

    def __str__(self):
        return self.team_name

Team.objects.filter().order_by('total_points')


