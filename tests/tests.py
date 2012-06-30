"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

from factories import PyMafiaUserFactory, GameFactory, PlayerFactory
from pymafia.models import Classification, Game, Player, PyMafiaUser


class UserTest(TestCase):


    def test_user_can_create_more_games(self):
        user = PyMafiaUserFactory()

        self.assertEquals(user.can_user_new_game(), True)

    def test_user_cant_create_more_games(self):
        user = PyMafiaUserFactory()

        PlayerFactory(user=user)
        PlayerFactory(user=user)

        self.assertEquals(user.can_user_new_game(), False)

    def test_user_current_games(self):
        game1 = GameFactory()
        game2 = GameFactory()

        user = PyMafiaUserFactory()

        PlayerFactory(user=user, game=game1)
        PlayerFactory(user=user, game=game2)

        self.assertEqual(list(user.get_current_games()), [game1, game2])



class GameTest(TestCase):
    pass
