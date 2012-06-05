from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    name = models.CharField(max_length=15)
    # amount of characters in the game
    max_size = models.PositiveSmallIntegerField()
    # the current game time.  0 = not started, 1 = day, 2 = night, 3 = day...
    time = models.PositiveSmallIntegerField()
    # How often the game changes cycle, in minutes
    period = models.PositiveSmallIntegerField()

class Skill(models.Model):
    name = models.CharField(max_length=8)
    ability = models.PositiveSmallIntegerField()

class Classification(models.Model):
    name = models.CharField(max_length=8)
    # True  = town, False  = mafia
    alignment = models.BooleanField()
    skill = models.ForeignKey(Skill)

class Character(models.Model):
    name = models.CharField(max_length=15)
    # true if alive, false if dead
    alive = models.BooleanField()
    user = models.ForeignKey(User)
    game = models.ForeignKey(Game)
    classification = models.ForeignKey(Classification)

class Action(models.Model):
    recorded_at = models.PositiveSmallIntegerField()
    character = models.ForeignKey(Character)
    skill = models.ForeignKey(Skill)
