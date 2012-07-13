"""URLS for pymafia"""

from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy

from views import (
                   ActionList, PlayerCreate, PlayerList,
                   GameCreate, GameDetail, GameList
                   )

urlpatterns = patterns('',
                url(
                    r'^game/$',
                    GameList.as_view(template_name='game_list.html'),
                    name='game_list'
                    ),
                url(
                    r'^game/(?P<pk>\d+)/$',
                    GameDetail.as_view(template_name='game_detail.html'),
                    name='game_detail'
                   ),
                url(
                    r'^game/create/$',
                    GameCreate.as_view(template_name='game_create.html'),
                    name='game_create'
                    ),

                url(
                    r'^game/(?P<game_id>\d+)/register/$',
                    PlayerCreate.as_view(template_name='player_create.html'),
                    name='player_create'
                   ),
                url(
                    r'^game/(?P<game_id>\d+)/player/$',
                    PlayerList.as_view(template_name='player_list.html'),
                    name='player_list'
                   ),
                url(
                    r'^game/(?P<pk>\d+)/action/$',
                    ActionList.as_view(template_name='action_list.html'),
                    name='action_list'
                   )
                )
