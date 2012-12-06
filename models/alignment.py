from django.db import models

class Alignment(models.Model):
    """Alignment Model"""
    name = models.CharField(max_length=15, help_text="Skill's displaying name")

    def __unicode__(self):
        """Used to pretty-print in the admin :-"""
        return (self.name)

    class Meta:
        app_label = 'pymafia'
