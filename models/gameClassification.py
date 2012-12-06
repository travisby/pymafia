from django.db import models
from pymafia.models import Classification, Game


class GameClassification(models.Model):
    """Skill Model"""

    classification = models.ForeignKey(Classification)
    game = models.ForeignKey(Game)
    count = models.PositiveSmallIntegerField()

    def __unicode__(self):
        """Used to pretty-print in the admin :-"""
        return ('%s %s' % (self.count, self.classification))

    class Meta:
        """This is so we can have multiple model files"""
        app_label = 'pymafia'
