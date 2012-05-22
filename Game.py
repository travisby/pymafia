class Game:
    
    def getVotes():
        pass

    def queueKill(self, killer, killed):
        killer.addPastMoves("Attempted to kill " + killed.getName())
        #TODO 
        #Add that player to some queue
    
    def queueProtect(self, protector, protected):
        protector.addPastMoves("Attempted to protect " + protected.getName())
        #TODO 
        #Set some flag that the player becomes unkillable.
        
    def queueJail(self, jailer, jailed):
        jailer.addPastMoves("Attempted to jail " + jailed.getName())
        #TODO
    
    def queueInvestigate(self, investigator, investigated):
        investigator.addPastMoves("Attempted to investigate " + investigated.getName())
        #TODO
    
    