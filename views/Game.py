from django.http import HttpResponse
import datetime

def create_game(request):
    if request.method == 'GET':
        # throw exception
        raise Http404
        # TODO
        # This shouldn't be a 404.
    elif request.method == 'POST':
        name = POST['name']
        #max_size = POST['max_size']
        max_size = 9
        time = 0
        period = POST['period']
        game = Game(name = name, max_size = maxSize, time = time, period =
                period)
        game.save()
        # TODO
        #load template for game.id


def register_game(request):
    if request.method == 'GET':
        # throw exception
        raise Http404
        # TODO
        # This shouldn't be a 404.
    elif request.method == 'POST':
        name = POST['name']
        userID = POST['userID']
        gameID = POST['gameID']
        character = Character(name = name, alive = 0, user = userID, game =
                gameID)
        character.save()
        
        # If there are enough players, start the game!
        if Player.get(game = gameID).count == Game.get(pk=gameID).max_size:
            # send start game signal
            #wait a small amount of time [so the start game goes through

        # TODO
        # load template for game.id

def start_game(gameID):
    game = Game.get(pk = gameID)
    players = Player.filter(game = game.id)
    if players.count != game.max_size:
        # throw exception
        raise Http404
        # this shouldn't be a 404.
    # TODO
    # this is where we should allow for as many game types as imaginable.
    classesReq = [1,1,1,1,1,2,3]
    classesOpt = [1,4,5,6]
    ###########################################
    random.shuffle(classesOpt)
    # After we shuffle the optional classes, we subtract the length of required
    # classes from the amount of players.  We then delete from THERE to the end
    # of the shuffled classesOpt list, to get our final list of Classifications
    del classesOpt[players.count-len(classesReq):len(classesOpt)]OD
    classesReq.extend(classesOpt)
    random.shuffle(classesReq)
    players = Player.filter(game = gameID)
    for player in players:
        player.alive =1
        # TODO
        # send notification
        player.classification = classifications.pop(0)
    Player.save()
    game.time = 1 
