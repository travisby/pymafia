from django.db import models
from skill import Skill


class Classification(models.Model):
    """All Game Classifications"""

    name = models.CharField(max_length=8, help_text='Class name')
    # True  = town, False  = mafia
    alignment = models.BooleanField(help_text='True = town, False = mafia')
    skill = models.ManyToManyField(Skill)

    class Meta:
        app_label = 'pymafia'