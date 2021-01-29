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
    
    def makeMove(self, pawn, newPos, boardSize):
        self.pawns[pawn] = newPos
        if self.pawns[pawn] >= boardSize: # if outside board
            print('outside board')
            del self.pawns[pawn]
    
    def findFurthestPawn(self, pawnsToMove):
        pawns = {i:j for i,j in self.pawns.items() if i in pawnsToMove} # get pawns from pawnstomove (probably ugly code)
        maxValue = max(pawns.values())
        furthestPawn = list(pawns.keys())[list(pawns.values()).index(maxValue)]
        oldPos = pawns[furthestPawn]
        
        return(furthestPawn)
        
    def findNewPos(self, pawn, stepsForward):
        oldPos = self.pawns[pawn]
        if oldPos != -1:
            newPos = oldPos + stepsForward
        else:
            newPos = 0
            
        return(oldPos, newPos)
    
    def findPawnsToMove(self, board, stepsForward):
        pawnsToMove = []
        if stepsForward == 6: # look first to open bridges
            pawnValues = {}
            for pawn in self.pawns:
                if self.pawns[pawn] not in pawnValues:
                    pawnValues[pawn] = 1
                else:
                    if pawnValues[pawn] == 1:
                        pawnsToMove.append(pawn)
                    pawnValues[pawn] += 1
        elif stepsForward == 5: # look first to go to startingPoint
            pawnsAtBase = [i for i,j in self.pawns.items() if j == 0]
            if len(pawnsAtBase) != 2:
                pawnsToMove = [i for i,j in self.pawns.items() if j == -1]
        blockedPawns = [] # maybe make already a set from blockedPawns
        if not pawnsToMove:
            pawnsToMove = [i for i,j in self.pawns.items() if j > -1]
            for pawn in pawnsToMove:
                bridge = False
                step = 0
                while bridge == False and step <= stepsForward:
                    step += 1
                    relPos = self.pawns[pawn] + step
                    pos = (relPos + self.startingPoint) % board.boardSize
                    if len(board.filledBoard[pos]) == 2:
                        bridge = True
                        blockedPawns.append(pawn)
                        
        return(list(set(pawnsToMove) - set(blockedPawns))) 
        
    
    #def performStrategy(self, strategy):


# the board keeps track where all the pawns of each player are + tells the special board positions
class Board: # now only the small board variant
    def __init__(self, boardSize):
        self.boardSize = boardSize
        self.filledBoard = [[] for i in range(boardSize)]
        self.startingPoints = []
        self.endPoints = []
        self.safeSpots = [] 
        for i in range(4):
            self.safeSpots.append(i * 17 + 5 - 1) # startingPoint, -1 to count 0 as a number
            self.safeSpots.append((i * 17 - 1) % boardSize) # endPoint
            self.safeSpots.append(i * 17 + 12 - 1)
            
    def makeMove(self, players, i, pawn, oldPosRel, newPosRel):
        newPos = (newPosRel + players[i].startingPoint) % self.boardSize
        oldPos = (oldPosRel + players[i].startingPoint) % self.boardSize
        
        if newPosRel == 0:
            self.filledBoard[newPos].append(pawn) # add
        elif newPosRel >= 68 or (newPosRel == -1 and newPosRel != oldPosRel):
            self.filledBoard[oldPos].remove(pawn) # remove
        elif newPosRel != oldPosRel and oldPosRel != -1: 
            self.filledBoard[newPos].append(pawn) # add  
            self.filledBoard[oldPos].remove(pawn) # remove
            
    def capturePawn(self, players, i, posRel): # capture when there is another player at the same position
        pos = (posRel + players[i].startingPoint) % self.boardSize
        capture = False
        if pos not in self.safeSpots and len(self.filledBoard[pos]) == 1: # should add another case when it is the startingPoint
            j = int(self.filledBoard[pos][0][6]) # other player on same pos
            if i != j:
                print('capture')
                capture = True
                players[j].makeMove(self.filledBoard[pos][0], -1, self.boardSize)
                self.filledBoard[pos].remove(self.filledBoard[pos][0])
                
        return(capture)
                
    
# should look into if the if's of makemove should be at a seperate function   
    
    
    
    