from django.db import models

class Player(models.Model):
    CLASS_CHOICES = [
        ('assassin', 'Assassin'),
        ('warrior', 'Warrior'),
        ('wizard', 'Wizard'),
        ('knight', 'Knight'),
        ('archer', 'Archer')
    ]

    name = models.CharField(max_length=100)
    classe = models.CharField(max_length=100, choices=CLASS_CHOICES)
    health = models.IntegerField(default=100)
    attack = models.IntegerField(default=10)
    experience = models.IntegerField(default=0)
    inventory = models.ManyToManyField('Inventory', blank=True)
    money = models.IntegerField(default=0)

    def __str__(self):
        return self.name

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