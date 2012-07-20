from lettuce import step, world
from nose.tools import assert_equal, assert_in
import json

from django.test import Client

from pymafia.tests.factories import *

# Helpers
client = Client()
URL = '/api/v1/'
JSON = '/?format=json'
world.games = []
world.classifications = [0, 1, 2, 3, 4, 5]
world.actions = []
world.players = []
def api_get(resource, kwargs=None):
    if kwargs:
        return json.loads(client.get(URL + resource + JSON, kwargs).content)
    else:
        return json.loads(client.get(URL + resource + JSON).content)
# Creators

@step(u'"([^"]*)" games exist')
def given_x_games_exist(step, num_games):
    for i in range(int(num_games)):
        world.games.append(GameFactory())

@step(u'"([^"]*)" actions exist')
def given_x_actions_exist(step, num_actions):
    for i in range(int(num_actions)):
        world.actions.append(ActionFactory())

@step(u'"([^"]*)" classifications exist')
def given_group1_classifications_exist(step, num_classifications):
    for i in range(int(num_classifications)):
        world.classifications.append(ClassificationFactory())

@step(u'"([^"]*)" players exist')
def and_group1_players_exist(step, num_players):
    if not world.games:
        # TODO totally legacy code
        given_x_games_exist(step, 1)
    for i in range(int(num_players)):
        world.players.append(PlayerFactory(game=world.games[0]))

# Test API calls

@step(u'the action is viewed')
def view_action(step):
    world.response = api_get('action', {'pk': 1})

@step(u'the actions are viewed')
def view_actions(step):
    world.response = api_get('action')

@step(u'the classification is viewed')
def view_classification(step):
    world.response = api_get('classification', {'pk': 1})

@step(u'the classifications are viewed')
def view_classifications(step):
    world.response = api_get('classification')

@step(u'the game is viewed')
def view_game(step):
    world.response = api_get('game', {'pk': 1})

@step(u'the games are viewed')
def view_games(step):
    world.response = api_get('game')

@step(u'the player is viewed')
def view_player(step):
    world.response = api_get('player', {'pk': 1})

@step(u'the players are viewed')
def view_players(step):
    world.response = api_get('player')


# Assertions

@step(u'Then the player is returned')
def then_the_player_is_returned(step):
    assert_equal(len(world.players), len(world.response['objects']))

@step(u'Then the players are returned')
def then_the_players_are_returned(step):
    assert_equal(len(world.players), len(world.response['objects']))

@step(u'the actions are returned')
def then_the_actions_are_returned(step):
    assert_equal(len(world.actions), len(world.response['objects']))

@step(u'the classifications are returned')
def then_the_classifications_are_returned(step):
    assert_equal(len(world.classifications), len(world.response['objects']))


@step(u'the games are returned')
def then_the_games_are_returned(step):
    assert_equal(len(world.games), len(world.response['objects']))

@step(u'the game is returned')
def then_the_game_is_returned(step):
    assert_equal(len(world.games), len(world.response['objects']))
