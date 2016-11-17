from django.shortcuts import render
from .models import Team

# Create your views here.




def get_leaderboard(request):
    teams = Team.objects.all()
    return render(request, 'leaderboard.html', {"teams":teams})

