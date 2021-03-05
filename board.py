# each player plays according to a certain strategy
# each player has 4 pawns of which each have a spot
# the pawns have a relative position from the player pov
# finds which pawns a player can use and moves them from player pov
class Player:
    def __init__(self, number, boardSize, strategy):
        self.number = number
        self.name = 'player' + str(number)
        self.strategy = strategy
        self.startingPoint = number * 17 + 5 - 1
        self.endPoint = (number * 17 - 1) % boardSize
        self.pawns = {}
        for i in range(4): # 4 pawns
            self.pawns[self.name + 'pawn' + str(i)] = -1 # not on the board yet
        self.pawnsHome = 4
        self.pawnsFinished = 0
    
    def makeMove(self, pawn, newPos, boardSize):
        if newPos == -1:
            self.pawnsHome += 1
        elif newPos == 0:
            self.pawnsHome -= 1
        self.pawns[pawn] = newPos
        if newPos >= (boardSize + 2): # if outside board, should be equal
            del self.pawns[pawn]
            self.pawnsFinished += 1
            
    def performStrategy(self, players, board, pawnsToMove, stepsForward):
        if self.strategy == 'furthest':
            pawnToMove = self.findFurthestPawn(pawnsToMove)
        elif self.strategy == 'safest':
            pawnToMove = self.findSafestMove(players, board, pawnsToMove, stepsForward)
            
        return(pawnToMove)
    
    def findFurthestPawn(self, pawnsToMove):
        pawns = {i:j for i,j in self.pawns.items() if i in pawnsToMove} # get pawns from pawnstomove (probably ugly code)
        maxValue = max(pawns.values())
        furthestPawn = list(pawns.keys())[list(pawns.values()).index(maxValue)]
        
        return(furthestPawn)
        
    def findSafestMove(self, players, board, pawnsToMove, stepsForward):
        safeScores = self.calcSafetyScores(players, board, pawnsToMove, stepsForward) # dont calculate when pawn is not on board 
        safestMove = max(safeScores, key=safeScores.get)
        safestMoves = []
        for safeScore in safeScores:
            if safeScores[safeScore] == safeScores[safestMove]:
                safestMoves.append(safeScore)
        if len(safestMoves) > 1:
            return(self.findFurthestPawn(safestMoves))
        else:
            return(safestMoves[0])
        
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
                    pawnValues[self.pawns[pawn]] = 1
                else:
                    if pawnValues[self.pawns[pawn]] == 1 and self.pawns[pawn] > -1:
                        pawnsToMove.append(pawn) # pawns in a bridge
                    pawnValues[self.pawns[pawn]] += 1
            pawnsToMove = self.findNonBlockedMoves(board, stepsForward, pawnsToMove)
        elif stepsForward == 5: # look first to go to startingPoint
            pawnsAtStart = [i for i,j in self.pawns.items() if j == 0]
            if len(pawnsAtStart) != 2:
                pawnsToMove = [i for i,j in self.pawns.items() if j == -1] 
                if pawnsToMove:
                    pawnsToMove = [pawnsToMove[0]] # more don't matter
        if not pawnsToMove:
            pawnsToMove = [i for i,j in self.pawns.items() if j > -1]
            print('pawnsToMove + blocked:', pawnsToMove)
            pawnsToMove = self.findNonBlockedMoves(board, stepsForward, pawnsToMove)
                        
        return(pawnsToMove)
        
    def findNonBlockedMoves(self, board, stepsForward, pawnsToMove):
        blockedPawns = [] # maybe make already a set from blockedPawns
        for pawn in pawnsToMove:
            bridge = False
            step = 1
            while bridge == False and step <= stepsForward:
                relPos = self.pawns[pawn] + step
                finishPos = relPos - (board.boardSize - 5)
                if finishPos < 0:
                    pos = (relPos + self.startingPoint) % board.boardSize
                    if len(board.filledBoard[pos]) == 2:
                        bridge = True
                        blockedPawns.append(pawn)
                elif finishPos < 7:
                    if len(board.filledFinishLine[self.number][finishPos]) == 2:
                        bridge = True
                        blockedPawns.append(pawn)
                step += 1
                    
        return(list(set(pawnsToMove) - set(blockedPawns)))
        
    def calcSafetyScores(self, players, board, pawnsToMove, stepsForward):
        otherPlNums = set(range(4)) - {self.number} # number of players is 4
        hasPawnsAtBase = {}
        hasBridges = {}
        for otherPlNum in otherPlNums:
            hasPawnsAtBase[otherPlNum] = bool([i for i,j in self.pawns.items() if j == -1])
            hasBridges[otherPlNum] = bool([i for i,j in enumerate(board.filledBoard) if len(j) == 2])
        safetyScore = {}
        for pawn in pawnsToMove:
            relPos = self.pawns[pawn]
            pos = (relPos + self.startingPoint) % board.boardSize
            posNew = (pos + stepsForward) % board.boardSize
            safetyRank = self.calcSafetyRank(players, board, stepsForward, pos, hasPawnsAtBase, hasBridges, False)
            safetyRankNew = self.calcSafetyRank(players, board, stepsForward, posNew, hasPawnsAtBase, hasBridges, True)
            safetyScore[pawn] = safetyRankNew - safetyRank
            
        return(safetyScore)

    def calcSafetyRank(self, players, board, stepsForward, pos, hasPawnsAtBase, hasBridges, futureMove):
        safetyRank = 0
        if pos in board.safeSpots or pos == self.startingPoint or pos > board.boardSize - 5:
            safetyRank = 1
        elif len(board.filledBoard[pos]) == 2 and pos not in board.startingPoints:
            safetyRank = 1
        elif futureMove and len(board.filledBoard[pos]) == 1 and pos not in board.startingPoints:
            if self.number == int(board.filledBoard[pos][0][6]): # future bridge, maybe it can be added with the if
                safetyRank = 1
        else:
            pawnsPerPlayerBehind = self.countPawnsBehind(players, board, stepsForward, pos, hasPawnsAtBase, hasBridges)
            for value in pawnsPerPlayerBehind.values():
                safetyRank = value / 6 + (1 - value / 6) * safetyRank
            safetyRank = 1 - safetyRank
        
        return(safetyRank)

    # players variable is not needed, can be read from board
    def countPawnsBehind(self, players, board, stepsForward, pos, hasPawnsAtBase, hasBridges):
        bridgeAtPos = False
        pawnsPerPlayerBehind = {}
        otherPlNums = set(range(4)) - {self.number}
        for otherPlNum in otherPlNums:
            pawnsPerPlayerBehind[otherPlNum] = 0
        for i in range(1,7): # should be 1,8 in the case when all pawns of another player are on board
            comPos = (pos - i) % board.boardSize
            pawnsBehind = board.filledBoard[comPos]
            if pawnsBehind:
                plNum2Prev = -1 # initialize
                for pawnBehind in pawnsBehind:
                    plNum2 = int(pawnBehind[6])  
                    if self.number != plNum2: # has to be other player
                        tryToCount = False
                        if (i == 5 and not hasPawnsAtBase[plNum2]) or (i == 6 and not hasBridges[plNum2]) or i < 5:
                            tryToCount = True
                        elif i == 6 and len(board.filledBoard[comPos]) == 2:
                            if plNum2 == int(board.filledBoard[comPos][1][6]):
                                tryToCount = True
                        if tryToCount:
                            relPos2 = players[plNum2].pawns[pawnBehind]
                            relPosNew2 = relPos2 + i + stepsForward
                            if relPosNew2 < board.boardSize and plNum2 != plNum2Prev:
                                pawnsPerPlayerBehind[plNum2] += 1
                    plNum2Prev = plNum2
        
        return(pawnsPerPlayerBehind)   

# the board keeps track where all the pawns of each player are + tells the special board positions
# executes moves on board
class Board: # now only the small board variant
    def __init__(self):
        self.boardSize = 68
        self.filledBoard = [[] for i in range(self.boardSize)]
        self.filledFinishLine = [[[] for i in range(7)] for i in range(4)]
        self.startingPoints = []
        self.endPoints = []
        self.safeSpots = []
        for i in range(4):
            self.startingPoints.append(i * 17 + 5 - 1) # startingPoints, -1 to count 0 as a number
            self.safeSpots.append((i * 17 - 1) % self.boardSize) # endPoints
            self.safeSpots.append(i * 17 + 12 - 1)
            
    def makeMove(self, players, i, pawn, oldPosRel, newPosRel):
        newPos = (newPosRel + players[i].startingPoint) % self.boardSize
        oldPos = (oldPosRel + players[i].startingPoint) % self.boardSize
        newPosFin = newPosRel - (self.boardSize - 5) # finish line pos
        if newPosFin < 0:
            if newPosRel == 0:
                self.filledBoard[newPos].append(pawn) # add board
            elif newPosRel == -1 and newPosRel != oldPosRel: # should be at exactly + 3
                self.filledBoard[oldPos].remove(pawn) # remove board
            elif newPosRel != oldPosRel and oldPosRel != -1: 
                self.filledBoard[newPos].append(pawn) # add board
                self.filledBoard[oldPos].remove(pawn) # remove board
        else:
            oldPosFin = oldPosRel - (self.boardSize - 5)
            if newPosFin > 6 and oldPosFin < 0:
                self.filledBoard[oldPos].remove(pawn) # remove board
            elif newPosFin >= 0 and oldPosFin < 0:
                self.filledFinishLine[i][newPosFin].append(pawn) # add finish
                self.filledBoard[oldPos].remove(pawn) # remove board
            elif newPosFin > 6:
                self.filledFinishLine[i][oldPosFin].remove(pawn) # remove finish
            elif newPosFin >= 0 and oldPosFin <= 6:
                self.filledFinishLine[i][newPosFin].append(pawn) # add finish
                self.filledFinishLine[i][oldPosFin].remove(pawn) # remove finish
            
    def capturePawn(self, players, i, posRel): # capture when there is another player at the same position        
        capture = False
        if posRel < self.boardSize - 5:
            pos = (posRel + players[i].startingPoint) % self.boardSize
            if pos not in self.safeSpots and pos not in self.startingPoints and len(self.filledBoard[pos]) == 1:
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