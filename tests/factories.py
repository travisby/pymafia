import uuid
from factory import Factory, SubFactory, LazyAttribute

from django.contrib.auth.models import User

from pymafia.models import Action, Alignment, Player, Classification, Game, Skill

class AlignmentFactory(Factory):
    FACTORY_FOR = Alignment

    name = LazyAttribute(lambda x:uuid.uuid1().__str__())

class SkillFactory(Factory):
    FACTORY_FOR = Skill

    name = LazyAttribute(lambda x:uuid.uuid1().__str__())


class ClassificationFactory(Factory):
    FACTORY_FOR = Classification

    name = LazyAttribute(lambda x:uuid.uuid1().__str__())

    alignment = SubFactory(AlignmentFactory)
    #skill = SubFactory(SkillFactory())


class UserFactory(Factory):
    FACTORY_FOR = User

    username = LazyAttribute(lambda x:uuid.uuid1().__str__())

class GameFactory(Factory):
    FACTORY_FOR = Game

    name = LazyAttribute(lambda x:uuid.uuid1().__str__())

    max_size = 9
    time = 0
    period = 24


class PlayerFactory(Factory):
    FACTORY_FOR = Player

    name = LazyAttribute(lambda x:uuid.uuid1().__str__())
    alive = True
    user = SubFactory(UserFactory)
    classification = SubFactory(ClassificationFactory)
    game = SubFactory(GameFactory)


class ActionFactory(Factory):
    FACTORY_FOR = Action

    time = 1
    player = SubFactory(PlayerFactory)
    skill = SubFactory(SkillFactory)







