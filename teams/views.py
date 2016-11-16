from django.shortcuts import render

# Create your views here.


def get_leaderboard(request):
    return render(request, 'index.html')
