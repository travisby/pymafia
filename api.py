from tastypie.resources import ModelResource
from tastypie.authorization import Authorization

from pymafia.models import Game, Action, Player, Classification, Alignment, Skill


class GameResource(ModelResource):
    class Meta:
        queryset = Game.objects.all()
        allowed_methods = ('get', 'post')
        authorization= Authorization()


class ActionResource(ModelResource):
    class Meta:
        queryset = Action.objects.all()
        allowed_methods = ('get', 'post')
        authorization= Authorization()


class PlayerResource(ModelResource):
    class Meta:
        queryset = Player.objects.all()
        fields = ('name', 'alive', 'game')
        allowed_methods = ('get',)
        authorization= Authorization()


class ClassificationResource(ModelResource):
    class Meta:
        queryset = Classification.objects.all()
        allowed_methods = ('get', 'post')
        authorization= Authorization()


class AlignmentResource(ModelResource):
    class Meta:
        queryset = Alignment.objects.all()
        allowed_methods = ('get',)
        authorization= Authorization()


class SkillResource(ModelResource):
    class Meta:
        queryset = Skill.objects.all()
        allowed_methods = ('get',)
        authorization= Authorization()
