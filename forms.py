from django.forms import ModelForm
from pymafia.models import Character, Game


class GameForm(ModelForm):
    class Meta:
        model = Game


class CharacterForm(ModelForm):
    class Meta:
        model = Character
