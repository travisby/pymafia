from django.db import models

from pymafia.models import Skill

class Alignment(models.Model):
    """Alignment Model"""
    name = models.CharField(max_length=15, help_text="Skill's displaying name")
    skill = models.ManyToManyField(Skill, blank=True)

    def __unicode__(self):
        """Used to pretty-print in the admin :-"""
        return (self.name)

    class Meta:
        """This is so we can have multiple model files"""
        app_label = 'pymafia'
