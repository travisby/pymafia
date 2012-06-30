from bootstrap.forms import BootstrapModelForm

from pymafia.models import Character, Game


class GameForm(BootstrapModelForm):
    """Create new Game Form"""
    class Meta:
        model = Game
        layout = ('Please fill out this quick form to start your game')


class CharacterForm(BootstrapModelForm):
    """Create new Character form"""
    class Meta:
        model = Character
