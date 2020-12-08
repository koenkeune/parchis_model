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
            self.pawns[self.name + 'pawn' + str(i)] = -1 # not on the board yet  
    
    # assumes that there are pawns left
    def makeMove(self, diceNumber, boardSize):
        maxValue = max(self.pawns.values())
        furthestPawn = list(self.pawns.keys())[list(self.pawns.values()).index(maxValue)]
        
        oldPos = self.pawns[furthestPawn]
        
        if self.pawns[furthestPawn] != -1:
            newPos = self.pawns[furthestPawn] + diceNumber
        elif diceNumber == 5:
            newPos = 0
        else:
            newPos = oldPos
            
        self.pawns[furthestPawn] = newPos
        
        if newPos >= boardSize: # if outside board
            del self.pawns[furthestPawn]
        
        
        #pawnsInBase = [i for i,j in pawns.items() if j == -1]
        
        # for pawn in pawnsToMove:
        # availableMoves = []
        
        return(furthestPawn, oldPos, newPos) # aka moved pawn
    
        
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
            self.filledBoard[endPoint].append('entrance spot') # and safe point
            self.filledBoard[startingPoint].append('starting point')
            self.filledBoard[i * 17 + 12 - 1].append('safe spot')
            
    def makeMoveOnBoard(self, player, movedPawn, oldPosRel, newPosRel): # doesnt work if the pawn is removed
        newPos = (newPosRel + player.startingPoint) % self.boardSize
        oldPos = (oldPosRel + player.startingPoint) % self.boardSize
        
        if newPosRel == 0:
            self.filledBoard[newPos].append(movedPawn) # add
        elif newPosRel >= 68:
            self.filledBoard[oldPos][self.filledBoard[oldPos].index(movedPawn)].remove(movedPawn) # remove
        elif (newPosRel != oldPosRel) | (oldPosRel != -1):
            self.filledBoard[newPos].append(movedPawn) # add
            self.filledBoard[oldPos][self.filledBoard[oldPos].index(movedPawn)].remove(movedPawn) # remove
       
    
        
    
# # a pawn has a position on the board    
# class Pawn(Player, Board):
    # def __init__(self, name, startingPoint):
        # self.startingPoint = startingPoint
        # self.name = name
        