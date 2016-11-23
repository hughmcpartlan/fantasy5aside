from django.shortcuts import render, redirect, get_object_or_404
from .models import Team
from .forms import CreateTeamForm
from django.contrib.auth.decorators import login_required
import csv
from django.http import HttpResponse, HttpResponseRedirect
from players.models import Defender, Midfielder, Striker


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

def get_viewprofile(request, id):
    team = get_object_or_404(Team, pk=id)
    return render(request, 'viewprofile.html', {'team': team})


def get_downloads(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="f5a-weeklydownload.csv"'

    writer = csv.writer(response)
    writer.writerow(['Player id', 'Full Name', 'Team Name', 'Position', 'Goals'])
    defenders = Defender.objects.all()
    for defender in defenders:
        writer.writerow([defender.id, defender.full_name, defender.team_name, 'D', 0])
    for midfielder in Midfielder.objects.all():
        writer.writerow([midfielder.id, midfielder.full_name, midfielder.team_name, 'M', 0])
    for striker in Striker.objects.all():
        writer.writerow([striker.id, striker.full_name, striker.team_name, 'S', 0])

    return response


def upload_csv(request):
    reset_gameweek_points()

    file = request.FILES['scoresheet']
    rows = [row for row in csv.reader(file.read().splitlines())]

    for row in rows[1::]:
        id, position, goals = row[0], row[3], row[4]
        update_teams_with_player(id, position, goals)


    return HttpResponse('File Uploaded')

def update_teams_with_player(id, position, goals):
    if goals > 0:
        if (position == 'D'):
            update_teams_with_defender(id, goals)
        elif (position == 'M'):
            update_teams_with_midfielder(id, goals)
        else:
            update_teams_with_striker(id, goals)


def reset_gameweek_points():
    teams = Team.objects.all()
    for team in teams:
        team.gameweek_points = 0
        team.save()

def update_teams_with_defender(id, goals):
    teams = Team.objects.filter(defender=id)
    for team in teams:
        team.gameweek_points += 3 * int(goals)
        team.total_points += 3 * int(goals)
        team.save()

def update_teams_with_midfielder(id, goals):
    teams = Team.objects.filter(midfielder1=id) | Team.objects.filter(midfielder2=id)
    for team in teams:
        team.gameweek_points += 2 * int(goals)
        team.total_points += 2 * int(goals)
        team.save()


def update_teams_with_striker(id, goals):
    teams = Team.objects.filter(striker1=id) | Team.objects.filter(striker2=id)
    for team in teams:
        team.gameweek_points += 2 * int(goals)
        team.total_points += 2 * int(goals)
        team.save()

def get_backup(request):
    return render(request, 'backup.html')





