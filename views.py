from django.views.generic import ListView, DetailView, CreateView

from models import Action, Player, Game, PyMafiaUser


class ActionList(ListView):
    """Lists all Actions in a game"""
    model = Action


class PlayerCreate(CreateView):
    """Renders a form to create a player for a game"""
    model = Player

    def get_form(self, form_class):
        form = super(PlayerCreate, self).get_form(form_class)
        # Some fun trickery to deal with py_mafia_user being a proxy of user
        form.instance.user = PyMafiaUser(pk=self.request.user.pk)
        print self.kwargs
        form.instance.game = get_extra_context['game']
        return form

class PlayerList(ListView):
    """Lists all players in the current game"""
    model = Player


class GameCreate(CreateView):
    """Renders a form to create a new game"""
    model = Game


class GameDetail(DetailView):
    """Details a game"""
    model = Game


class GameList(ListView):
    """Lists all games"""
    model = Game
