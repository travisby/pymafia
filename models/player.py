from django.db import models
from django.contrib.auth.models import User

from pymafia.models import Classification, Game


class Player(models.Model):
    """All of the Players"""

    name = models.CharField(max_length=15, help_text="Character's name")
    # true if alive, false if dead
    alive = models.BooleanField(default=False, editable='False', help_text='Is alive Boolean')
    user = models.ForeignKey(User, editable='False')
    game = models.ForeignKey(Game, editable='False')
    classification = models.ForeignKey(Classification, blank=True, null=True, editable=False)

    def __unicode__(self):
        """Used to pretty-print in the admin :-"""
        return (self.name)

    def can_register(self):
        return False

    class Meta:
        """This is so we can have multiple model files"""
        app_label = 'pymafia'
