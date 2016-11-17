from django.shortcuts import render
from .models import Team

# Create your views here.




def get_leaderboard(request):
    teams = Team.objects.all().order_by('-total_points')
    return render(request, 'leaderboard.html', {"teams":teams})


