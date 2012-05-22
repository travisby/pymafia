import Player


class Doctor(Player):

    def __init__(self):
        super(Doctor, self).__init__()
        
    def jail(self, player):
        Game.queueJail(self, player)
