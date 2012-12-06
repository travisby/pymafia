from django.db import models

class Skill(models.Model):
    """Skill Model"""
    name = models.CharField(max_length=8, help_text="Skill's displaying name")

    def __unicode__(self):
        """Used to pretty-print in the admin :-"""
        return (self.name)

    class Meta:
        """This is so we can have multiple model files"""
        app_label = 'pymafia'
