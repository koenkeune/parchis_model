# set up the game (based on the initial parameters)


# each player plays according to a certain strategy
# each player has 4 pawns of which each have a spot on the board
class Player:
    def __init__(self, strategy, startingPoint, endPoint):
            self.strategy = strategy
            self.startingPoint = startingPoint
            self.endPoint = endPoint
            numberOfPawns = 4
            self.pawns = {}
            for i in range(1,numberOfPawns+1):
                self.pawns['pawn' + str(i)] = -1 # not on the board yet
            
    
    
    
    
    
    #def performStrategy(self, strategy):
    
    #def getFurthestPawn():


###### initialize board

# the board keeps track where all the pawns of each player are
class Board: # now only the small board variant

    ### initializing part ###
    boardSize = 68
    boardWithoutPlayers = [[] for i in range(boardSize)]
    playerNames = ['P1', 'P2', 'P3', 'P4']
    pawns = 4
    players = list()
    for i in range(4):
        startingPoint = i * 17 + 5 - 1 # -1 to count 0 as a number
        endPoint = (i * 17 - 1) % boardSize 
        boardWithoutPlayers[endPoint] = 'entrance spot' # and safe point
        boardWithoutPlayers[startingPoint] = 'starting point '
        boardWithoutPlayers[i * 17 + 12 - 1] = 'safe spot'
        players.append(Player('random', startingPoint, endPoint))
        
    
    #########################

    
    

        
    
# a pawn has a position on the board    
class Pawn(Player, Board):
    def __init__(self, name, startingPoint):
        self.startingPoint = startingPoint
        self.name = name

    

    
# #board[17] = 


# ######



# playing = True



#   while (playing)
#    for (player in players)
        