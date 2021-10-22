from random import randrange
from visualizer import *
import pygame, sys
from pygame.locals import *
from board import *
import copy
    
class game:
    def __init__(self, strategies):
        self.players = list()
        self.board = Board()
        self.players.append(Player(0, self.board.boardSize, strategies[0]))
        self.players.append(Player(1, self.board.boardSize, strategies[1]))
        self.players.append(Player(2, self.board.boardSize, strategies[2]))
        self.players.append(Player(3, self.board.boardSize, strategies[3]))
        self.winner = -1
        self.steps = 0
    
    def simGame(self): # sims one game
        someoneWon = False
        numPlayers = len(self.players)
        while not(someoneWon):
            i = 0
            self.steps += 1
            while not(someoneWon) and i < numPlayers:
                sixesThrown = 0
                diceNumber = 6 # to get in the while
                while diceNumber == 6 and not(someoneWon):
                    diceNumber = randrange(1,7)
                    if diceNumber == 6:
                        sixesThrown += 1
                    stepsForward = diceNumber
                    capture = True
                    while capture:
                        capture = False
                        pawnsToMove = self.players[i].findPawnsToMove(self.board, stepsForward)
                        if pawnsToMove:
                            if len(pawnsToMove) == 1: # or at the same pos
                                pawn = pawnsToMove[0]
                            else:
                                pawn = self.players[i].performStrategy(self.players, self.board, pawnsToMove, stepsForward) # move in head
                            positions = self.players[i].findNewPos(pawn, stepsForward) # move in head
                            if sixesThrown == 3 and positions[1] < self.board.boardSize: # remove only if it didn't land in the end zone
                                self.players[i].makeMove(pawn, -1, self.board.boardSize)
                                self.board.makeMove(self.players, i, pawn, positions[0], -1) # can only remove if it is on the board
                            else:
                                self.players[i].makeMove(pawn, positions[1], self.board.boardSize) # move in head
                                capture = self.board.capturePawn(self.players, i, positions[1])
                                self.board.makeMove(self.players, i, pawn, positions[0], positions[1]) # move in real life
                                if capture:
                                    stepsForward = 20
                    if sixesThrown == 3:
                        diceNumber = 0 # a number to get out of the while loop 
                    someoneWon = (len(self.players[i].pawns) == 0) # not(self.pawns)
                if someoneWon:
                    self.winner = i
                i += 1
    
    def playGame(self): # plays one game
        pygame.init()
        W = 800
        H = 800
        screen = pygame.display.set_mode((W, H))
        drawBoard(screen, W, H)
        screen_copy = screen.copy()
        drawPawnsAtHome(screen, self.players)
        
        someoneWon = False
        numPlayers = len(self.players)
        t = throwDiceForStart(numPlayers)
        sixesThrown = 0
        capture = False
        canThrowAgain = False
        waitingForMove = False
        
        while True:
            nextStep = False
            key1 = False
            key2 = False
            key3 = False
            key4 = False
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYUP:
                    if event.key == K_SPACE or event.key == K_RETURN:
                        nextStep = True
            
            pygame.display.update()
            
            if nextStep and not waitingForMove: # and not players[t].strategy == 'player'
                if capture:
                    capture = False
                else:    
                    diceNumber = randrange(1,7)
                    stepsForward = diceNumber
                    if diceNumber == 6: # go again
                        canThrowAgain = True
                        sixesThrown += 1
                        if sixesThrown == 3:
                            canThrowAgain = False
                    else:
                        canThrowAgain = False
                
                print(self.board.filledBoard)
                print(getPlayerColorString(t), 'can move:', stepsForward)
                
                # repeat if capture
                pawnsToMove = self.players[t].findPawnsToMove(self.board, stepsForward)
                print('pawns to move:', pawnsToMove)
                if pawnsToMove:
                    if self.players[t].strategy == 'player': # draw virtual moves and let the player pick a move
                        finishedVirtual = []
                        virtualBoard = copy.deepcopy(self.board)
                        for i in range(len(pawnsToMove)):
                            positions = self.players[t].findNewPos(pawnsToMove[i], stepsForward)
                            if positions[1] < self.board.boardSize - 5:
                                pos = (positions[1] + self.players[t].startingPoint) % self.board.boardSize
                                virtualBoard.filledBoard[pos].append(self.players[t].name + 'VirtualMove' + str(i+1))
                            elif positions[1] < self.board.boardSize + 2:
                                pos = positions[1] - (self.board.boardSize - 5)
                                virtualBoard.filledFinishLine[t][pos].append(self.players[t].name + 'VirtualMove' + str(i+1))
                            else:
                                finishedVirtual.append(i+1)
                        
                        print(virtualBoard.filledBoard )
                        print(self.board.filledFinishLine)
                        print(virtualBoard.filledFinishLine)
                        screen.blit(screen_copy, (0,0))
                        drawPawnsOnBoard(screen, virtualBoard.filledBoard)
                        drawPawnsAtHome(screen, self.players)
                        drawPawnsAtFinishline(screen, virtualBoard.filledFinishLine)
                        drawFinishedPawns(screen, self.players)
                        drawFinishedVirtualMoves(screen, self.players, t, finishedVirtual)
                        pygame.display.update()
                        
                        pawnNumber = False
                        while not pawnNumber:
                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    pygame.quit()
                                    sys.exit()
                                elif event.type == KEYUP:
                                    if event.key == K_1:
                                        key1 = True
                                    elif event.key == K_2:
                                        key2 = True
                                    elif event.key == K_3:
                                        key3 = True
                                    elif event.key == K_4:
                                        key4 = True
                            pawnNumber = getPawnNumber(len(pawnsToMove), [key1, key2, key3, key4])
                        pawn = pawnsToMove[pawnNumber-1]
                    else:
                        if len(pawnsToMove) == 1: # or at the same pos
                            pawn = pawnsToMove[0]
                        else:
                            pawn = self.players[t].performStrategy(self.players, self.board, pawnsToMove, stepsForward) # move in head
                    print('will move:', pawn)
                    positions = self.players[t].findNewPos(pawn, stepsForward) # move in head
                    if sixesThrown == 3 and positions[1] < self.board.boardSize: # remove only if it didn't land in the end zone
                        self.players[t].makeMove(pawn, -1, self.board.boardSize)
                        self.board.makeMove(self.players, t, pawn, positions[0], -1) # can only remove if it is on the board
                    else:
                        self.players[t].makeMove(pawn, positions[1], self.board.boardSize) # move in head
                        capture = self.board.capturePawn(self.players, t, positions[1])
                        self.board.makeMove(self.players, t, pawn, positions[0], positions[1]) # move in real life
                        if capture:
                            stepsForward = 20
                            
                someoneWon = (len(self.players[t].pawns) == 0) # not(self.pawns)
                if someoneWon:
                    self.winner = self.players[t].name
                    print(self.players[t].name, 'HAS WON!!!')
                
                # print('capture?', capture, 'can throw again?', canThrowAgain)
                
                if not(capture) and not(canThrowAgain):
                    t += 1
                    self.steps += 1
                    if t >= numPlayers:
                        t = 0
                    sixesThrown = 0
                if canThrowAgain:
                    canThrowAgain = False
                
                # redraw:
                screen.blit(screen_copy, (0,0))
                drawPawnsOnBoard(screen, self.board.filledBoard)
                drawPawnsAtHome(screen, self.players)
                drawPawnsAtFinishline(screen, self.board.filledFinishLine)
                drawFinishedPawns(screen, self.players)
                
# extra functions for game.play():                
def throwDiceForStart(numPlayers):
    thrownNumber = [[i,0] for i in range(numPlayers)]

    while len(thrownNumber) > 1:
        for i in range(len(thrownNumber)):
            diceNumber = randrange(1,7)
            thrownNumber[i][1] = diceNumber
            print(getPlayerColorString(thrownNumber[i][0]), 'rolled', diceNumber)  
        highestDice = max([elem[1] for elem in thrownNumber])
        thrownNumber = [[num, dice] for num, dice in thrownNumber if dice == highestDice]
        
    print(getPlayerColorString(thrownNumber[0][0]), 'starts the game')

    return(thrownNumber[0][0])
                
def getPlayerColorString(playerNum):
    if playerNum == 0:
        return('yellow')
    elif playerNum == 1:
        return('blue')
    elif playerNum == 2:
        return('red')
    elif playerNum == 3:
        return('green')
        
def getPawnNumber(numberOfOptions, numberPressed):
    pawnNumber = False
    for i in range(numberOfOptions):
        if numberPressed[i] == True:
            pawnNumber = i + 1
    
    return(pawnNumber)
    
