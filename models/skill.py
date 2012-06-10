from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=8, help_text="Skill's displaying name")
    ability = models.PositiveSmallIntegerField(help_text='Defined ability')

    class Meta:
        app_label = 'pymafia'
