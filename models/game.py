from django.db import models
from pymafia.models import Character


class Game(models.Model):
    name = models.CharField(max_length=15, help_text='Game name')
    # amount of characters in the game
    max_size = models.PositiveSmallIntegerField(default=9, help_text='Amount of players')
    # the current game time.  0 = not started, 1 = day, 2 = night, 3 = day...
    time = models.PositiveSmallIntegerField(default=0, editable=False, help_text='Current time')
    # How often the game changes cycle, in hours
    period = models.PositiveSmallIntegerField(default=24, help_text='Time, in hours, for the max phase time')

    # TODO refactor name.  Used here and in the character model
    def can_user_create_game(self, user):
        return len(user.character_set.all.filter(alive=1)) < 1

    def clean(self):
        from django.core.exceptions import ValidationError
        if not self.can_user_create_game(Character(game=self).values()[0].user):
            raise ValidationError

    class Meta:
        app_label = 'pymafia'
