from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
def get_index(request):
    return render(request, 'index.html')

def get_about(request):
    return render(request, 'about.html')

@login_required
def get_manage(request):
    if not request.user.is_superuser:
        return HttpResponse('The user is not superuser')
    else:
        return render(request, 'manage.html')

def get_nav(request):
    return render(request, 'navbar.html')


