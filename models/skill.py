from django.db import models

class Skill(models.Model):
    """Skill Model"""
    name = models.CharField(max_length=8, help_text="Skill's displaying name")

    def __unicode__(self):
        return (self.name)

    class Meta:
        app_label = 'pymafia'
