from django.shortcuts import render, redirect, get_object_or_404
from .models import Team
from .forms import CreateTeamForm
from django.contrib.auth.decorators import login_required
import csv
from django.http import HttpResponse

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
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    writer = csv.writer(response)
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    return response