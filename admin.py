from django.contrib import admin
from pymafia.models import (
                            Alignment, Action, Player,
                            Classification, Game, Skill, GameClassification
                            )

admin.site.register(Action)
admin.site.register(Alignment)
admin.site.register(Classification)
admin.site.register(Game)
admin.site.register(Player)
admin.site.register(Skill)
admin.site.register(GameClassification)
