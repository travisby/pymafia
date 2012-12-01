from tastypie.resources import ModelResource

from pymafia.models import Game, Action, Player, Classification, Alignment, Skill


class GameResource(ModelResource):
    class Meta:
        queryset = Game.objects.all()


class ActionResource(ModelResource):
    class Meta:
        queryset = Action.objects.all()


class PlayerResource(ModelResource):
    class Meta:
        queryset = Player.objects.all()


class ClassificationResource(ModelResource):
    class Meta:
        queryset = Classification.objects.all()


class AlignmentResource(ModelResource):
    class Meta:
        queryset = Alignment.objects.all()


class SkillResource(ModelResource):
    class Meta:
        queryset = Skill.objects.all()
