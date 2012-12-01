from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie import fields

from django.contrib.auth.models import User


from pymafia.models import Game, Action, Player, Classification, Alignment, Skill


class UserResource(ModelResource):
    players = fields.ToManyField('pymafia.api.PlayerResource', attribute = lambda x : x.obj.player_set.all())

    class Meta:
        queryset = User.objects.all()
        fields = ('date_joined', 'email', 'first_name', 'id', 'is_active', 'is_staff', 'last_login', 'last_name', 'players', 'username')
        resource_name = 'user'
        allowed_methods = ('get', 'post', 'put')
        authorization = Authorization()


class PlayerResource(ModelResource):
    user = fields.ToOneField(UserResource, 'user')

    class Meta:
        queryset = Player.objects.all()
        fields = ('name', 'alive', 'game', 'user')
        allowed_methods = ('get',)
        authorization= Authorization()


class GameResource(ModelResource):
    players = fields.OneToManyField(PlayerResource, attribute = lambda x : x.obj.player_set.all())

    class Meta:
        queryset = Game.objects.all()
        fields = ('id', 'max_size', 'name', 'period', 'players', 'time')
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


class ClassificationResource(ModelResource):
    skills = fields.ToManyField(SkillResource, attribute = lambda x : x.obj.skill.all())
    alignment = fields.ToOneField(AlignmentResource, 'alignment')

    class Meta:
        queryset = Classification.objects.all()
        fields = ('id', 'name', 'alignment', 'skills')
        allowed_methods = ('get', 'post')
        authorization= Authorization()


class ActionResource(ModelResource):
    skill = fields.ForeignKey(SkillResource, 'skill')
    performed_against_player = fields.ToOneField(PlayerResource, 'performed_against_player')

    class Meta:
        queryset = Action.objects.all()
        allowed_methods = ('get', 'post')
        authorization= Authorization()
        fields = ('time', 'skill', 'performed_against_player')
