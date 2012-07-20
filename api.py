from tastypie.resources import ModelResource, Resource, ALL

from pymafia.models import *


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
