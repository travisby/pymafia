"""
Set the models up for adminning
"""

from django.contrib import admin
import pymafia.models

admin.site.register(pymafia.models.Action)
admin.site.register(pymafia.models.Alignment)
admin.site.register(pymafia.models.Game)
admin.site.register(pymafia.models.Klass)
admin.site.register(pymafia.models.Player)
admin.site.register(pymafia.models.Setup)
admin.site.register(pymafia.models.SetupKlass)
admin.site.register(pymafia.models.Skill)
