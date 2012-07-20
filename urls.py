"""URLS for pymafia"""

from django.conf.urls.defaults import *
from tastypie.api import Api
from pymafia.api import GameResource, ActionResource, PlayerResource, ClassificationResource

v1_api = Api()

v1_api.register(GameResource())
v1_api.register(ActionResource())
v1_api.register(PlayerResource())
v1_api.register(ClassificationResource())

urlpatterns = patterns('',
    (r'', include(v1_api.urls)),
)
