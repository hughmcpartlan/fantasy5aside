from django.shortcuts import render
from .models import Team
from .forms import CreateTeamForm
from django.contrib.auth.decorators import login_required

# Create your views here.




def get_leaderboard(request):
    teams = Team.objects.all().order_by('-total_points')
    return render(request, 'leaderboard.html', {"teams":teams})


def create_team(request):
    if request.method == "post":

    else:
        form = CreateTeamForm(request.POST)
        return render(request, 'createteam.html', {'form':form})

@login_required(login_url='/login/')
def profile(request):
    return render(request, 'profile.html')