from django.shortcuts import render, redirect
from .forms import PlayerForm
from .models import Player

def home(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('game')
    else:
        form = PlayerForm()
    return render(request, 'index.html', {'form': form})

def game_view(request):
    player = Player.objects.last()
    return render(request, 'gaming/game.html', {'player': player})