from lettuce import before, after, world
from django.test.utils import setup_test_environment, teardown_test_environment
from django.core.management import call_command
from django.db import connection

@before.harvest
def initial_setup(server):
    call_command('syncdb', interactive=False, verbosity=1)
    call_command('flush', interactive=False, verbosity=0)
    call_command('loaddata', 'all', verbosity=0)


@after.each_scenario
def reset_data(scenario):
    # Clean up django.
    call_command('flush', interactive=False, verbosity=0)
    call_command('loaddata', 'all', verbosity=0)
    world.response = None
    world.games = []
    world.actions = []
    world.players = []
    world.classifications = [0, 1, 2, 3, 4, 5]
