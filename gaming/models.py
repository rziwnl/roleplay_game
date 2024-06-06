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
    experience = models.IntegerField(default=0)
    money = models.IntegerField(default=0)

    def __str__(self):
        return self.name
