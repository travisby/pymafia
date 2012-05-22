class Player:

    roles = None
    alive = None
    availableMoves = []
    pastMoves = []
    notes = []
    name = None
    password = None
    
    def __init__(self):
        #TODO
        #Add everyone, and some getters/setters
        pass
    
    def vote(self, player):
        player.votedOn(self)
        
    def checkVotes(self):
        return Game.getVotes()
    
    def votedOn(self, player):
        #TODO
        pass
    
    def getPastMoves(self):
        return pastMoves
    
    def talk(self):
        #TODO
        pass
    
    def notes(self):
        #TODO
        pass
    
    def addPastMoves(self, addage):
        pastMoves += addage
        #TODO 
        #Make sure each move is added to the DB!
        