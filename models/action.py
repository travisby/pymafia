from django.db import models

from pymafia.models import Player, Skill


class Action(models.Model):
    """Records all actions (voting, kills, etc), by game and characters"""

    time = models.PositiveSmallIntegerField(help_text='Recorded time of action')
    performing_player = models.ForeignKey(Player, help_text='Peforming Character', related_name='performing_player')
    skill = models.ForeignKey(Skill, help_text='Used skill')
    performed_against_player = models.ForeignKey(Player, help_text='Player that the skill was used on', related_name='performed_against_player')

#    def __unicode__(self):
#        return (self.player + self.skill)

    class Meta:
        app_label = 'pymafia'
