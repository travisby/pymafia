from django.db import models
from django.contrib.auth.models import User
from game import Game
from classification import Classification


class Character(models.Model):
    name = models.CharField(max_length=15, help_text="Character's name")
    # true if alive, false if dead
    alive = models.BooleanField(default=0, editable='False', help_text='Is alive Boolean')
    user = models.ForeignKey(User, editable='False')
    game = models.ForeignKey(Game, editable='False')
    classification = models.ForeignKey(Classification, blank=True, editable=False)

    def clean(self):
        from django.core.exceptions import ValidationError
        if not Game.can_user_create_game(self.user):
            raise ValidationError

    class Meta:
        app_label = 'pymafia'
