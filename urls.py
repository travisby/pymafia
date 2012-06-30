"""URLS for pymafia"""

from django.conf.urls import patterns, url

from views import (
                   ActionList, PlayerCreate, PlayerList,
                   GameCreate, GameDetail, GameList
                   )

# urlpatterns = patterns('',
#                        url(r'^api/', include(tastyapi.urls))
# )

urlpatterns = patterns('',
                url(r'^game/$',
                    GameList.as_view()),
                url(r'^game/create/$',
                    GameCreate.as_view()),
                url(r'^game/(?P<game_id>\d+)/$',
                   GameDetail.as_view()),
                url(r'^game/(?P<game_id>\d+)/register/$',
                   CharacterCreate.as_view()),
                url(r'^game/(?P<game_id>\d+)/action/$',
                   ActionList.as_view()),
                url(r'^game/(?P<game_id>\d+)/character/$',
                   CharacterList.as_view()),
                )
