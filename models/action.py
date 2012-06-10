from django.db import models
from character import Character
from skill import Skill
class Action(models.Model):
    time = models.PositiveSmallIntegerField(help_text='Recorded time of action')
    character = models.ForeignKey(Character, help_text='Peforming Character')
    skill = models.ForeignKey(Skill, help_text='Used skill')

    class Meta:
        app_label = 'pymafia'
