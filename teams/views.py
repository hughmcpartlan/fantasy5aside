from django.shortcuts import render, redirect
from .models import Team
from .forms import CreateTeamForm
from django.contrib.auth.decorators import login_required

# Create your views here

def create_team(request):
    if request.method == "POST":
        form = CreateTeamForm(request.POST)

        if form.is_valid():
            team = form.save(commit=False)
            team.owner = request.user
            team.save()
            return redirect(profile)
    else:
        form = CreateTeamForm()

    return render(request, 'createteam.html', {'form':form})

@login_required(login_url='/login/')
def profile(request):
    return render(request, 'profile.html')

def get_leaderboard(request):
    teams = Team.objects.all().order_by('-total_points')
    return render(request, 'leaderboard.html', {"teams":teams})