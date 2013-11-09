"""
Models for Django
"""

from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):

    """
    Individual game of pymafia
    """

    setup = models.ForeignKey('Setup')

    name = models.CharField(max_length=15)


class Setup(models.Model):

    """
    The type of game happening, E.X. C9
    """

    klasses = models.ManyToManyField('Klass', through='SetupKlass')

    name = models.CharField(max_length=15)
    num_players = models.PositiveSmallIntegerField()
    is_start_time_day = models.BooleanField()
    setup_type = models.CharField(
        max_length=1,
        choices=(
            ('1', 'Open'),
            ('2', 'SemiOpen'),
            ('3', 'Closed')
        )
    )


class SetupKlass(models.Model):

    """
    Klass available in a setup, e.g. 4 doctors
    """

    setup = models.ForeignKey('Setup')
    klass = models.ForeignKey('Klass')

    priority = models.PositiveSmallIntegerField()


class Klass(models.Model):

    """
    Individual klasses available for a game, e.g. Sane cop
    """

    # already completed in Setup
    # models.ManyToManyField('Setup', through='SetupKlass')
    models.ManyToManyField('Skill')
    models.ForeignKey('Alignment')

    name = models.CharField(max_length=15)


class Alignment(models.Model):

    """
    Good/bad, townie/etc.
    """

    models.ManyToManyField('Skill')

    models.CharField(max_length=15)


class Skill(models.Model):

    """
    Abilities that klass and alignments have
    """

    # already completed in Klass
    # klasses = models.ManyToManyField('Klass')
    # already completed in Alignment
    # models.ManyToManyField('Alignment')

    name = models.CharField(max_length=15)
    is_active = models.BooleanField()


class Player(models.Model):

    """
    A user participating in one game
    """

    game = models.ForeignKey('Game')
    user = models.ForeignKey(User)
    klass = models.ForeignKey('Klass')


class Action(models.Model):

    """
    Actions taken by a player (optionally) upon another
    """

    executor = models.ForeignKey('Player', related_name='actions_as_executor')
    target = models.ForeignKey('Player', related_name='actions_as_target')
    skill = models.ForeignKey('Skill')
