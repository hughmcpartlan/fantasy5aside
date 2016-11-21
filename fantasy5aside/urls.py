"""fantasy5aside URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from home.views import get_index, get_about, get_manage, get_nav
from accounts.views import register, login, logout, get_csv
from products.views import all_products
from teams.views import get_leaderboard, profile, create_team, get_viewprofile, get_downloads

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', get_index, name='index'),
    url(r'^about/', get_about, name='about'),
    url(r'^register/$', register, name='register'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^products/$', all_products),
    url(r'^leaderboard/', get_leaderboard, name='leaderboard'),
    url(r'^createteam/', create_team),
    url(r'^csv/', get_csv),
    url(r'^manage/', get_manage, name='manage'),
    url(r'^downloads/', get_downloads, name='download_scorelist'),
    url(r'^(?P<id>\d+)/$', get_viewprofile, name='viewprofile'),
    url(r'^nav/', get_nav)

]
