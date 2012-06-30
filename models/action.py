from django.db import models

from pymafia.models import Player, Skill


class Action(models.Model):
    """Records all actions (voting, kills, etc), by game and characters"""

    time = models.PositiveSmallIntegerField(help_text='Recorded time of action')
    player = models.ForeignKey(Player, help_text='Peforming Character')
    skill = models.ForeignKey(Skill, help_text='Used skill')

    class Meta:
        app_label = 'pymafia'
