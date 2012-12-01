from django.db import models

class Game(models.Model):
    """The Game model"""
    name = models.CharField(max_length=15, help_text='Game name')
    # amount of characters in the game
    max_size = models.PositiveSmallIntegerField(default=9, editable=False, help_text='Amount of players')
    # the current game time.  0 = not started, 1 = day, 2 = night, 3 = day...
    time = models.PositiveSmallIntegerField(default=0, editable=False, help_text='Current time')
    # How often the game changes cycle, in hours
    period = models.PositiveSmallIntegerField(default=24, help_text='Time, in hours, for the max phase time')

#    @models.permalink
#    def get_absolute_url(self):
#        return ('game_detail', [str(self.id)])

    def __unicode__(self):
        return '%s - %s' % (self.name, self.id)

    class Meta:
        app_label = 'pymafia'


# def start_game(gameID):
#     characters = Character.objects.filter(game=game.id)

    # TODO
    # this is where we should allow for as many game types as imaginable.
    # classesReq = [1, 1, 1, 1, 1, 2, 3]
    # classesOpt = [1, 4, 5, 6]
    ###########################################
    # random.shuffle(classesOpt)
    # This is the most efficient way I could think to generate a random list
    # of the above classes, when not all in classesOpt will be used
    # del classesOpt[characters.count() - len(classesReq):len(classesOpt)]
    # classesReq.extend(classesOpt)
    # random.shuffle(classesReq)
    # character = Character.filter(game=gameID)
    # with transaction.commit_on_success():
    #     for character in characters:
    #         character.alive = 1
    #         # TODO
    #         # send notification
    #         character.classification = classifications.pop(0)
    #         character.save()
    # game.time = 1
    # game.save()
