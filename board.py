from random import randrange
# set up the game (based on the initial parameters)

# each player plays according to a certain strategy
# each player has 4 pawns of which each have a spot
# the pawns have a relative position from the player pov
# finds which pawns a player can use and moves them from player pov
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
            pawnsAtStart = [i for i,j in self.pawns.items() if j == 0]
            if len(pawnsAtStart) != 2:
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
        
    def calcSafetyScores(self, players, board, moves, plNum, stepsForward):
        allPlayerNums = set(range(1,5)) # number of players
        otherPlNums = allPlayerNums - set(plNum)
        hasPawnsAtBase = {}
        hasBridges = {}
        for otherPlNum in otherPlNums:
            hasPawnsAtBase[otherPlNum] = bool([i for i,j in self.pawns.items() if j == -1])
            hasBridges[otherPlNum] = bool([i for i,j in enumerate(board.filledBoard) if len(j) == 2])
                
        safetyScore = {}
        for pawn in moves:
            relPos = self.pawn[pawn]
            pos = (relPos + self.startingPoint) % board.boardSize
            posNew = (pos + stepsForward) % board.boardSize
            
            safetyRank = calcSafetyRank(players, board, plNum, stepsForward, pos, hasPawnsAtBase, hasBridges)
            safetyRankNew = calcSafetyRank(players, board, plNum, stepsForward, posNew, hasPawnsAtBase, hasBridges)
            safetyScore[pawn] = safetyRankNew - safetyRank
            
        return(safetyScores)
  
    def calcSafetyRank(players, board, plNum, stepsForward, pos, hasPawnsAtBase, hasBridges):
        if pos in board.safeSpots:
            safetyRank = 1
        else:
            pawnsPerPlayerBehind = countPawnsBehind(players, board, plNum, stepsForward, pos, hasPawnsAtBase, hasBridges)
            safetyRank = 0
            for value in pawnsPerPlayerBehind.values():
                safetyRank = safetyRank + (1 - safetyRank) * value
                
        return(safetyRank)
    
    def countPawnsBehind(players, board, plNum, stepsForward, pos, hasPawnsAtBase, hasBridges): # should maybe be in board object
        pawnsPerPlayerBehind = {}
        
        for i in range(6): # should be 7 in the case when all pawns of another player are on board
            comPos = (pos - i) % board.boardSize
            pawnsBehind = board.filledBoard[comPos]
            if pawnsBehind:
                plNum2Prev = -1
                for pawnBehind in pawnsBehind:
                    plNum2 = int(board.filledBoard[pos][0][6])  
                    if plNum != plNum2:
                        if (i == 5 and not hasPawnsAtBase[plNum2]) or (i == 6 and not hasBridges[plNum2]) or i < 5: # should prob be rewritten
                            relPos2 = players[plNum2].pawns[pawnBehind]
                            relPosNew2 = relPos2 + i + stepsForward
                            if relPosNew2 < board.boardSize and plNum2 != plNum2Prev:
                                pawnsPerPlayerBehind[plNum2] += 1
                    plNum2Prev = plNum2
        
        return(pawnsPerPlayerBehind)
        
                 
            
        
    #def findCaptureMoves()
    
    
    
    #def performStrategy(self, strategy):


# the board keeps track where all the pawns of each player are + tells the special board positions
# executes moves on board
class Board: # now only the small board variant
    def __init__(self, boardSize):
        self.boardSize = boardSize
        self.filledBoard = [[] for i in range(boardSize)]
        self.startingPoints = []
        self.endPoints = []
        self.safeSpots = [] 
        for i in range(4):
            self.startingPoints.append(i * 17 + 5 - 1) # startingPoints, -1 to count 0 as a number
            self.safeSpots.append((i * 17 - 1) % boardSize) # endPoints
            self.safeSpots.append(i * 17 + 12 - 1)
            
    def makeMove(self, players, i, pawn, oldPosRel, newPosRel):
        newPos = (newPosRel + players[i].startingPoint) % self.boardSize
        oldPos = (oldPosRel + players[i].startingPoint) % self.boardSize
        
        if newPosRel == 0:
            self.filledBoard[newPos].append(pawn) # add
        elif newPosRel >= self.boardSize or (newPosRel == -1 and newPosRel != oldPosRel):
            self.filledBoard[oldPos].remove(pawn) # remove
        elif newPosRel != oldPosRel and oldPosRel != -1: 
            self.filledBoard[newPos].append(pawn) # add  
            self.filledBoard[oldPos].remove(pawn) # remove
            
    def capturePawn(self, players, i, posRel): # capture when there is another player at the same position        
        capture = False
        if posRel < self.boardSize:
            pos = (posRel + players[i].startingPoint) % self.boardSize
            if pos not in self.safeSpots and len(self.filledBoard[pos]) == 1:
                j = int(self.filledBoard[pos][0][6]) # other player on same pos
                if i != j:
                    capture = True
                    players[j].makeMove(self.filledBoard[pos][0], -1, self.boardSize)
                    self.filledBoard[pos].remove(self.filledBoard[pos][0])
            elif pos in self.startingPoints and len(self.filledBoard[pos]) == 2:
                j = int(self.filledBoard[pos][0][6])
                k = int(self.filledBoard[pos][1][6])
                if i != k: # capture last pawn first
                    capture = True
                    players[k].makeMove(self.filledBoard[pos][1], -1, self.boardSize)
                    self.filledBoard[pos].remove(self.filledBoard[pos][1])
                elif i != j:
                    capture = True
                    players[j].makeMove(self.filledBoard[pos][0], -1, self.boardSize)
                    self.filledBoard[pos].remove(self.filledBoard[pos][0])
            
        return(capture)
                
    
# should look into if the if's of makemove should be at a seperate function   
    
    
    
    