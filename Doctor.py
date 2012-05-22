import Player


class Cop(Player):

    def __init__(self):
        super(Cop, self).__init__()
        
    def protect(self, player):
        Game.queueProtect(self, player)