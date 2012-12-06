from django.db import models
from pymafia.models import Alignment, Skill

class Classification(models.Model):
    """All Game Classifications"""

    name = models.CharField(max_length=25, help_text='Class name')
    alignment = models.ForeignKey(Alignment)
    skill = models.ManyToManyField(Skill, blank=True)

    def __unicode__(self):
        """Used to pretty-print in the admin :-"""
        return (self.name)


    class Meta:
        """This is so we can have multiple model files"""
        app_label = 'pymafia'
