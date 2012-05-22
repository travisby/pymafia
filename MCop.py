import Cop


class MCop(Cop):
    
    friends = []

    def __init__(self):
        super(MCop, self).__init__()
        
    def viewFriends(self):
        return friends