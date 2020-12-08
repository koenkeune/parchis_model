from random import randrange
# set up the game (based on the initial parameters)

# each player plays according to a certain strategy
# each player has 4 pawns of which each have a spot
# the pawns have a relative position from the player pov
class Player:
    def __init__(self, number, boardSize, strategy):
        self.name = 'player' + str(number)
        self.strategy = strategy
        self.startingPoint = number * 17 + 5 - 1
        self.endPoint = (number * 17 - 1) % boardSize 
        numberOfPawns = 4
        self.pawns = {}
        for i in range(numberOfPawns):
            self.pawns['pawn' + str(i)] = -1 # not on the board yet  
    
    # should still check if there are pawns left
    def makeMove(self, diceNumber, boardSize): # not sure if i should add board, keep everything in player, or keep everything in board
        maxValue = max(self.pawns.values())
        furthestPawn = list(self.pawns.keys())[list(self.pawns.values()).index(maxValue)]
        
        
        if self.pawns[furthestPawn] != -1:
            self.pawns[furthestPawn] += diceNumber
        elif diceNumber == 5:
            self.pawns[furthestPawn] = 0
            
        if self.pawns[furthestPawn] >= boardSize: # if outside board
            del self.pawns[furthestPawn]
        
        
        #pawnsInBase = [i for i,j in pawns.items() if j == -1]
        
        # for pawn in pawnsToMove:
        # availableMoves = []
        
        
        
        
        
        
        
    # def makeMoveOnBoard(self, movedPawn, board): # should be moved to board class
        # if self.pawns[movedPawn] >= 68
        # del
        # posOnBoard = (self.pawns[movedPawn] + self.startingPoint) % 68
        # board[posOnBoard] = movedPawn
        
        # return(board)
        
    #def availableMoves(self, diceNumber):
    
    #def performStrategy(self, strategy):
    
    #def getFurthestPawn():


# the board keeps track where all the pawns of each player are + tells the special board positions
class Board: # now only the small board variant

    def __init__(self, boardSize):
        self.boardSize = boardSize
        self.filledBoard = [[] for i in range(boardSize)]
        for i in range(4):
            startingPoint = i * 17 + 5 - 1 # -1 to count 0 as a number
            endPoint = (i * 17 - 1) % boardSize 
            self.filledBoard[endPoint] = 'entrance spot' # and safe point
            self.filledBoard[startingPoint] = 'starting point '
            self.filledBoard[i * 17 + 12 - 1] = 'safe spot'
    
    

        
    
# # a pawn has a position on the board    
# class Pawn(Player, Board):
    # def __init__(self, name, startingPoint):
        # self.startingPoint = startingPoint
        # self.name = name
        