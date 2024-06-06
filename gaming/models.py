from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    health = models.IntegerField(default=100)
    experience = models.IntegerField(default=0)
    money = models.IntegerField(default=0)

    def __str__(self):
        return self.name
