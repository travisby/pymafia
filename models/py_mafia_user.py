from django.contrib.auth.models import User

from pymafia.models import Game, Player

class PyMafiaUser(User):
    """Proxy model for the User model in auth"""
    class Meta:
        proxy = True
        app_label = 'pymafia'


#    def get_alive_players(self):
#        """Returns all alive characters for a User"""
#        return Player.objects.filter(user=self, alive=True)

#    def get_current_games(self):
#        """Returns the games where the User has an alive character"""
#        return Game.objects.filter(player__in=self.get_alive_players())


#    def get_current_games_count(self):
#        """Returns the count of games where the User has alive an character"""
#        # We use get_alive_characters, which should have the same count
#        # as get_current_games(), but lets us skip an extra query
#        return self.get_alive_players().count()

#    def can_user_new_game(self):
#        """Returns True if the user can create or join a new game"""
#        return self.get_current_games_count() < 1
