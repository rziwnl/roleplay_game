from django.db import models

class Player(models.Model):
    CLASS_CHOICES = [
        ('assassin', 'Assassin'),
        ('warrior', 'Warrior'),
        ('wizard', 'Wizard'),
        ('knight', 'Knight'),
        ('archer', 'Archer')
    ]

    CLASS_STATS = {
        'assassin': {'health': 75, 'attack': 35},
        'warrior': {'health': 120, 'attack': 20},
        'wizard': {'health': 80, 'attack': 50},
        'knight': {'health': 150, 'attack': 25},
        'archer': {'health': 90, 'attack': 30},
    }

    name = models.CharField(max_length=100)
    classe = models.CharField(max_length=100, choices=CLASS_CHOICES)
    health = models.IntegerField(default=100)
    attack = models.IntegerField(default=10)
    experience = models.IntegerField(default=0)
    inventory = models.ManyToManyField('Inventory', blank=True)
    money = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.pk:  
            stats = self.CLASS_STATS.get(self.classe, {'health': 100, 'attack': 10})
            self.health = stats['health']
            self.attack = stats['attack']
        super(Player, self).save(*args, **kwargs)

class Inventory(models.Model):
    item_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.item_name
    

class Market(models.Model):
    item = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.item.item_name} - {self.price} coins"
    

class Monster(models.Model):
    name = models.CharField(max_length=100)
    health = models.IntegerField(default=50)
    attack = models.IntegerField(default=5)
    loot = models.CharField(max_length=100, default="Common item")

    def __str__(self):
        return self.name