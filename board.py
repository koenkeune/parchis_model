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
    def findFurthestPawn(self, pawnsToMove, diceNumber):
        # should remove self
        # should check if pawns are available to move
        # might remove else remove = oldPos
        # should be able to return nothing if there are no moves to be had
        
        pawns = {i:j for i,j in self.pawns.items() if i in pawnsToMove} # get pawns from pawnstomove (probably ugly code)
        
        maxValue = max(pawns.values())
        furthestPawn = list(pawns.keys())[list(pawns.values()).index(maxValue)]
        oldPos = pawns[furthestPawn]
        
        if pawns[furthestPawn] != -1:
            newPos = pawns[furthestPawn] + diceNumber
        elif diceNumber == 5: # the if check should be redundant because diceNumber should always be 5 when it comes there
            newPos = 0
        
        return(furthestPawn, oldPos, newPos)
        
    def findPawnsToMove(self, diceNumber):
        if diceNumber == 5:
            pawnsToMove = [i for i,j in self.pawns.items() if j == -1]
            if not pawnsToMove:
                pawnsToMove = [i for i,j in self.pawns.items() if j > -1]
        else:
            pawnsToMove = [i for i,j in self.pawns.items() if j > -1]
        
        return(pawnsToMove)
        
    
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
            
    def makeMove(self, player, pawn, oldPosRel, newPosRel): # doesnt work if the pawn is removed
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
        