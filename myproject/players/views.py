from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import PlayerForm
from .models import Player


def create_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            # Save the player (course handicaps will be calculated automatically)
            form.save()
            return redirect('player_menu_page.html')  # Redirect to a page listing all players (or another page as needed)
    else:
        form = PlayerForm()
    
    return render(request, 'players/create_player.html', {'form': form})

def player_list(request):
    players = Player.objects.all()
    return render(request, 'players/player_list.html', { 'players' : players})

def players_menu_page(request):
    #return render(request, 'players/players_menu_page.html', { 'posts' : posts})
    return render(request, 'players/players_menu_page.html', { 'players_menu_page' : players_menu_page})