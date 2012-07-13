from django.test import TestCase
from django.test.client import RequestFactory
from django.core.urlresolvers import reverse

from factories import ActionFactory, AlignmentFactory, ClassificationFactory, UserFactory, GameFactory, PlayerFactory, SkillFactory
from pymafia.models import Classification, Game, Player, PyMafiaUser
from pymafia.views import PlayerCreate

class UserTest(TestCase):


    def test_user_can_create_more_games(self):
        user = UserFactory()

        self.assertEquals(user.can_user_new_game(), True)

    def test_user_cant_create_more_games(self):
        user = UserFactory()

        PlayerFactory(user=user)
        PlayerFactory(user=user)

        self.assertEquals(user.can_user_new_game(), False)

    def test_user_current_games(self):
        game1 = GameFactory()
        game2 = GameFactory()

        user = UserFactory()

        PlayerFactory(user=user, game=game1)
        PlayerFactory(user=user, game=game2)

        self.assertEquals(list(user.get_current_games()), [game1, game2])



class GameTest(TestCase):

    def test_create_game(self):
        self.assertEquals(True, True)


class ToUnicodeTest(TestCase):

    def test_action(self):
        action = ActionFactory()

        self.assertEquals(action.__unicode__(), action.player.name + action.skill.name)

    def test_alignment(self):
        alignment = AlignmentFactory()

        self.assertEquals(alignment.__unicode__(), alignment.name)

    def test_classification(self):
        classification = ClassificationFactory()

        self.assertEquals(classification.__unicode__(), classification.name)

    def test_game(self):
        game = GameFactory()

        self.assertEquals(game.__unicode__(), game.name + unicode(game.id))

    def test_player(self):
        player = PlayerFactory()

        self.assertEquals(player.__unicode__(), player.name + unicode(player.id))

    def test_skill(self):
        skill = SkillFactory()

        self.assertEquals(skill.__unicode__(), skill.name)

class URLTest(TestCase):

    def test_game_detail(self):
        game = GameFactory()
        resp = self.client.get(game.get_absolute_url(), kwargs={'pk': 1})

        self.assertEqual(resp.status_code, 200)


class ViewTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_should_add_extra_fields_for_player_create(self):
        # Instantiate view
        user = UserFactory()
        game = GameFactory()
        request = self.factory.get(
                                    reverse(
                                            'player_create',
                                            kwargs={'game_id': game.id}
                                            ),
                                   kwargs={'game_id': game.id}
                                   )
        request.user = user
        print request.GET.get('kwargs', {})
        playerCreate = PlayerCreate.as_view()(request)
        form = playerCreate.get_form()
        # {'name': 'testUser'}
        self.assertEqual((form.user, form.game), (user, game))
