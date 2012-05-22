import Player


class Cop(Player):

    def __init__(self):
        super(Cop, self).__init__()
        
    def investigate(self, player):
        Game.queueInvestigate(self, player)
        pass