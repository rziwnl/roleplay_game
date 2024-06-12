import random
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .forms import PlayerForm
from .models import Item, Player, Monster


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
    monsters = list(Monster.objects.all())
    if not monsters:
        messages.error(request, "Aucun monstre disponible pour le combat.")
        return redirect('main')
    monster = random.choice(monsters)
    return redirect('battle', monster_id=monster.id)


def battle(request, monster_id):
    player = Player.objects.last()  # Récupère le dernier joueur créé
    monster = get_object_or_404(Monster, id=monster_id)

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'attack':
            monster.health -= player.attack
            if monster.health <= 0:
                player.experience += 10
                loot_item, created = Item.objects.get_or_create(name=monster.loot,
                                                                defaults={'description': f"Loot from {monster.name}"})
                player.inventory.add(loot_item)
                player.save()
                messages.success(request,
                                 f'You defeated {monster.name} and win 10 exp. You pick up {monster.loot}!')
                monster.delete()
                return redirect('main')
            else:
                player.health -= monster.attack
                if player.health <= 0:
                    player.health = 100  # Reset player health for simplicity
                    return redirect('home')
                player.save()
                monster.save()
        elif action == 'flee':
            return redirect('main')
    return render(request, 'gaming/battle.html', {'player': player, 'monster': monster})


def show_inventory(request):
    player = Player.objects.last()
    inventory = player.inventory.all()
    return render(request, 'gaming/inventory.html', {'player': player, 'inventory': inventory})
