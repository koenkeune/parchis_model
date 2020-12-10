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
    
    def makeMove(self, pawn, pos, boardSize):
        self.pawns[pawn] = pos
        if pos >= boardSize: # if outside board
            del self.pawns[pawn]
    
    # assumes that there are pawns left    
    def moveFurthestPawn(self, diceNumber):
        maxValue = max(self.pawns.values())
        furthestPawn = list(self.pawns.keys())[list(self.pawns.values()).index(maxValue)]
        oldPos = self.pawns[furthestPawn]
        
        if self.pawns[furthestPawn] != -1:
            newPos = self.pawns[furthestPawn] + diceNumber
        elif diceNumber == 5: # should always put it down if you can
            newPos = 0
        else:
            newPos = oldPos
        
        return(furthestPawn, oldPos, newPos)
        
    #def availableMoves(self, diceNumber):
        #pawnsInBase = [i for i,j in pawns.items() if j == -1]
        
        # for pawn in pawnsToMove:
        # availableMoves = []
    
    #def performStrategy(self, strategy):
    
    #def getFurthestPawn():


# the board keeps track where all the pawns of each player are + tells the special board positions
class Board: # now only the small board variant
    def __init__(self, boardSize):
        self.boardSize = boardSize
        self.filledBoard = [[] for i in range(boardSize)]
        self.startingPoint = []
        self.endPoint = []
        self.safeSpot = [] 
        for i in range(4):
            self.startingPoint.append(i * 17 + 5 - 1) # -1 to count 0 as a number
            self.endPoint.append((i * 17 - 1) % boardSize)
            self.safeSpot.append(i * 17 + 12 - 1)
            
    def makeMoveOnBoard(self, player, pawn, oldPosRel, newPosRel): # doesnt work if the pawn is removed
        newPos = (newPosRel + player.startingPoint) % self.boardSize
        oldPos = (oldPosRel + player.startingPoint) % self.boardSize
        
        if newPosRel == 0:
            self.filledBoard[newPos].append(pawn) # add
        elif newPosRel >= 68 or (newPosRel == -1 and newPosRel != oldPosRel):
            self.filledBoard[oldPos].remove(pawn) # remove
        elif newPosRel != oldPosRel and oldPosRel != -1: 
            self.filledBoard[newPos].append(pawn) # add  
            self.filledBoard[oldPos].remove(pawn) # remove
            
    
        
    
# # a pawn has a position on the board    
# class Pawn(Player, Board):
    # def __init__(self, name, startingPoint):
        # self.startingPoint = startingPoint
        # self.name = name
        