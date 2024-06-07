# gaming/views.py
import random
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PlayerForm
from .models import Player, Monster, Inventory, Market

def home(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = PlayerForm()
    return render(request, 'index.html', {'form': form})

def main(request):
    player = Player.objects.last() 
    return render(request, 'gaming/main.html', {'player': player})

def game_view(request):
    player = Player.objects.last() 
    return render(request, 'gaming/game.html', {'player': player})

def fight_monster(request):
    player = Player.objects.last() 
    monsters = list(Monster.objects.all())
    monster = random.choice(monsters) 
    return redirect('battle', monster_id=monster.id)

def battle(request, monster_id):
    player = Player.objects.last()  
    monster = get_object_or_404(Monster, id=monster_id)
    
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'attack':
            monster.health -= player.attack
            if monster.health <= 0:
                monster.delete()
                return redirect('main')
            else:
                player.health -= monster.attack
                if player.health <= 0:
                    player.health = 100 
                    return redirect('home')
                player.save()
                monster.save()
        elif action == 'flee':
            return redirect('main')
    return render(request, 'gaming/battle.html', {'player': player, 'monster': monster})