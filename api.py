from tastypie.resources import ModelResource

from pymafia.models import Game, Action, Player, Classification, Alignment, Skill


class GameResource(ModelResource):
    class Meta:
        queryset = Game.objects.all()
        allowed_methods = ('get', 'post')


class ActionResource(ModelResource):
    class Meta:
        queryset = Action.objects.all()
        allowed_methods = ('get', 'post')


class PlayerResource(ModelResource):
    class Meta:
        queryset = Player.objects.all()
        fields = ('name', 'alive', 'game')
        allowed_methods = ('get',)


class ClassificationResource(ModelResource):
    class Meta:
        queryset = Classification.objects.all()
        allowed_methods = ('get', 'post')


class AlignmentResource(ModelResource):
    class Meta:
        queryset = Alignment.objects.all()
        allowed_methods = ('get',)


class SkillResource(ModelResource):
    class Meta:
        queryset = Skill.objects.all()
        allowed_methods = ('get',)
