import Player


class Goon(Player):
    
    friends = []

    def __init__(self):
        super(Goon, self).__init__()
        #TODO
        #add friends
        pass
    
    def kill(self, player):
        Game.queueKill(self, player)
        
    def viewFriends(self):
        return friends