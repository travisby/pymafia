from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie import fields

from django.contrib.auth.models import User


from pymafia.models import Game, Action, Player, Classification, Alignment, Skill


class UserResource(ModelResource):
    players = fields.ManyToManyField('pymafia.api.resources.PlayerResource', 'players')

    class Meta:
        queryset = User.objects.all()
        fields = ('date_joined', 'email', 'first_name', 'id', 'is_active', 'is_staff', 'last_login', 'last_name', 'players' )
        resource_name = 'user'
        allowed_methods = ('get', 'post', 'put')
        authorization = Authorization()


class GameResource(ModelResource):
    class Meta:
        queryset = Game.objects.all()
        allowed_methods = ('get', 'post')
        authorization= Authorization()


class PlayerResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Player.objects.all()
        fields = ('name', 'alive', 'game', 'user')
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


class ActionResource(ModelResource):
    skill = fields.ForeignKey(SkillResource, 'skill')
    class Meta:
        queryset = Action.objects.all()
        allowed_methods = ('get', 'post')
        authorization= Authorization()
        fields = ('time', 'skill')
