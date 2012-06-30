from factory import Factory, SubFactory

from pymafia.models import Action, Player, Classification, Game, Skill
from pymafia.models import PyMafiaUser


class SkillFactory(Factory):
    FACTORY_FOR = Skill

    name = 'test_skill'
    ability = 1


class ClassificationFactory(Factory):
    FACTORY_FOR = Classification

    name = 'test_class'
    alignment = True
    #skill = SubFactory(SkillFactory())


class PyMafiaUserFactory(Factory):
    FACTORY_FOR = PyMafiaUser


class GameFactory(Factory):
    FACTORY_FOR = Game

    name = 'test_game'
    max_size = 9
    time = 0
    period = 24


class PlayerFactory(Factory):
    FACTORY_FOR = Player

    name = 'test_player'
    alive = True
    user = SubFactory(PyMafiaUserFactory)
    classification = SubFactory(ClassificationFactory)
    game = SubFactory(GameFactory)


class ActionFactory(Factory):
    FACTORY_FOR = Action

    time = 1
    player = SubFactory(PlayerFactory)
    skill = SubFactory(SkillFactory)







