from django.views.generic import ListView, DetailView, CreateView

from models import Action, Character, Game


class ActionList(ListView):
    """Lists all Actions in a game"""
    model = Action


class PlayerCreate(CreateView):
    """Renders a form to create a player for a game"""
    model = Character


class PlayerList(ListView):
    """Lists all players in the current game"""
    model = Character


class GameCreate(CreateView):
    """Renders a form to create a new game"""
    model = Game


class GameDetail(DetailView):
    """Details a game"""
    model = Game


class GameList(ListView):
    """Lists all games"""
    model = Game
