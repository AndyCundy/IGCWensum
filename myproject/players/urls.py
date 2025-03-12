# urls.py
from django.urls import path
from . import views

app_name = 'players'

urlpatterns = [
    path('create_player.html', views.create_player, name='create_player'),
    path('player_list.html', views.player_list, name="player_list"),
    path('player_menu_page.html', views.players_menu_page, name="players_menu_page"),
    
]
