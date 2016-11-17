from django.shortcuts import render
from .models import Player

# Create your views here.
def get_defenders(request):
    defenders =  Player.object.find(position='defender')
    return render(request, {'defenders':defenders})

def get_midfielders(request):
    midfielders =  Player.object.find(position='midfielder')
    return render(request, {'midfielders':midfielders})

def get_strikers(request):
    strikers =  Player.object.find(position='striker')
    return render(request, {'strikers':strikers})
