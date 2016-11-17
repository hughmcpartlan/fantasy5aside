from django import forms
from django.core.exceptions import ValidationError
from players.models import Player


class CreateTeamForm(forms.Form):

    defenders = [ (player.id, player.full_name) for player in Player.objects.filter(position='Defender')]
    midfielders = [ (player.id, player.full_name) for player in Player.objects.filter(position='Midfielder')]
    strikers = [ (player.id, player.full_name) for player in Player.objects.filter(position='Striker')]

    name = forms.CharField(max_length=100)
    team_name = forms.CharField(max_length=100)
    defender = forms.ChoiceField(label='defender', choices=defenders)
    midfielder1 = forms.ChoiceField(label='midfielder1', choices=midfielders)
    midfielder2 = forms.ChoiceField(label='midfielder2', choices=midfielders)
    striker1 = forms.ChoiceField(label='striker1', choices=strikers)
    striker2 = forms.ChoiceField(label='striker2', choices=strikers)



