from django.db import migrations, models

def create_monsters(apps, schema_editor):
    Monster = apps.get_model('gaming', 'Monster')
    monsters = [
        {"name": "Goblin", "health": 30, "attack": 5, "loot": "Goblin Ear"},
        {"name": "Orc", "health": 50, "attack": 10, "loot": "Orc Tusk"},
        {"name": "Dragon", "health": 200, "attack": 50, "loot": "Golden Scale"},
        {"name": "Troll", "health": 70, "attack": 15, "loot": "Troll Club"},
        {"name": "Vampire", "health": 60, "attack": 20, "loot": "Vampire Fang"},
        {"name": "Werewolf", "health": 80, "attack": 25, "loot": "Werewolf Fur"},
        {"name": "Skeleton", "health": 25, "attack": 5, "loot": "Bone Fragment"},
        {"name": "Zombie", "health": 40, "attack": 7, "loot": "Rotten Flesh"},
        {"name": "Cyclops", "health": 120, "attack": 30, "loot": "Cyclops Eye"},
        {"name": "Mummy", "health": 50, "attack": 10, "loot": "Ancient Bandage"},
        {"name": "Phoenix", "health": 100, "attack": 40, "loot": "Phoenix Feather"},
        {"name": "Hydra", "health": 150, "attack": 35, "loot": "Hydra Scale"},
    ]
    for monster in monsters:
        Monster.objects.create(**monster)

class Migration(migrations.Migration):

    dependencies = [
        ('gaming', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='monster',
            name='loot',
            field=models.CharField(default='Common item', max_length=100),
        ),
        migrations.RunPython(create_monsters),
    ]