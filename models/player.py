from django.db import models
from django.contrib.auth.models import User

from pymafia.models import Classification, Game, PyMafiaUser


class Player(models.Model):
    """All of the Players"""

    name = models.CharField(max_length=15, help_text="Character's name")
    # true if alive, false if dead
    alive = models.BooleanField(default=False, editable=False, help_text='Is alive Boolean')
    classification = models.ForeignKey(Classification, blank=True, null=True, editable=False)
    game = models.ForeignKey(Game, editable=False)
    user = models.ForeignKey(PyMafiaUser, editable=False)


    def __unicode__(self):
        return (self.name + unicode(self.id))

    class Meta:
        app_label = 'pymafia'
