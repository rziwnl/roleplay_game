from django.db import migrations

def create_monsters(apps, schema_editor):
    Monster = apps.get_model('gaming', 'Monster')
    monsters = [
        {"name": "Goblin", "health": 30, "attack": 5},
        {"name": "Orc", "health": 50, "attack": 10},
        {"name": "Dragon", "health": 200, "attack": 50},
        {"name": "Troll", "health": 70, "attack": 15},
    ]
    for monster in monsters:
        Monster.objects.create(**monster)

class Migration(migrations.Migration):

    dependencies = [
        ('gaming', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_monsters),
    ]
