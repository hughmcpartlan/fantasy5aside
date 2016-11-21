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
        writer.writerow([defender.id, defender.full_name, defender.team_name, 'D'])
    for midfielder in Midfielder.objects.all():
        writer.writerow([midfielder.id, midfielder.full_name, midfielder.team_name, 'M'])
    for striker in Striker.objects.all():
        writer.writerow([striker.id, striker.full_name, 'S', striker.team_name, 'S'])

    return response


def upload_csv(request):
    file = request.FILES['scoresheet']
    reader = csv.reader(file)
    my_list = []
    defenders = []
    midfielders = []
    strikers = []
    return HttpResponse(file.name)





# def update_weekly_points(request):
#
#     teams = Team.objects.all()
#     defenders = Defender.objects.all()
#     midfielders = Midfielder.objects.all()
#     strikers = Striker.objects.all()
#     team_weekly_total =[]
#
#     for team in teams:
#         for defender in defenders:
#             if defender.full_name in team:
#                 if goals >0:
#                     team_weekly_total.append(goals*3)
#         for midfielder in midfielders:
#             if midfielder.full_name in team:
#                 if goals >0:
#                     team_weekly_total.append(goals*2)
#         for striker in strikers:
#             if striker.full_name in team:
#                 team_weekly_total.append(goals)
#
#     return



