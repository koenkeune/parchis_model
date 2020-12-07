from random import randrange
# set up the game (based on the initial parameters)

# each player plays according to a certain strategy
# each player has 4 pawns of which each have a spot
# the pawns have a relative position from the player pov
class Player:
    def __init__(self, number, strategy, startingPoint, endPoint):
        self.name = 'player' + str(number)
        self.strategy = strategy
        self.startingPoint = startingPoint
        self.endPoint = endPoint
        numberOfPawns = 4
        self.pawns = {}
        for i in range(numberOfPawns):
            self.pawns['pawn' + str(i)] = -1 # not on the board yet  
    
    # should still check if there are pawns left
    def makeMove(self, diceNumber): # not sure if i should add board, keep everything in player, or keep everything in board
        maxValue = max(self.pawns.values())
        furthestPawn = list(self.pawns.keys())list(self.pawns.values()).index(maxValue)
        
        
        
        if pawns[furthestPawn] != -1:
            self.pawns[furthestPawn] += diceNumber
        elif diceNumber == 5:
            self.pawns[furthestPawn] = 0
            
        if self.pawns[furthestPawn] > 68:
            del self.pawns[furthestPawn]
        
        
        #pawnsInBase = [i for i,j in pawns.items() if j == -1]
        
        # for pawn in pawnsToMove:
            
        
        # availableMoves = []
        
        
        
        
        # pawnName = pawnsToMove[0]
        # board[self.pawns[pawnName]] = self.name + '_' + pawnName
        # self.pawns[pawnName] = self.startingPoint
         
        
    #def availableMoves(self, diceNumber):
    
    #def performStrategy(self, strategy):
    
    #def getFurthestPawn():


# initialize board

# the board keeps track where all the pawns of each player are
def board(): # now only the small board variant

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
        players.append(Player(i, 'random', startingPoint, endPoint))
        

    return(boardWithoutPlayers, players)
    
    

        
    
# # a pawn has a position on the board    
# class Pawn(Player, Board):
    # def __init__(self, name, startingPoint):
        # self.startingPoint = startingPoint
        # self.name = name

    

    
# #board[17] = 


# ######



# playing = True



#   while (playing)
#    for (player in players)
        