import pygame, os, sys, copy
from pygame.locals import *
from random import randrange
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__)) # make sure it can be called from testing
sys.path.append(os.path.dirname(SCRIPT_DIR))
from model.board import *
from model.visualizer import *
    
class Game:
    def __init__(self, strategies):
        self.players = list()
        self.board = Board()
        self.players.append(Player(0, self.board.boardSize, strategies[0]))
        self.players.append(Player(1, self.board.boardSize, strategies[1]))
        self.players.append(Player(2, self.board.boardSize, strategies[2]))
        self.players.append(Player(3, self.board.boardSize, strategies[3]))
        self.winner = -1
        self.steps = 1
        self.canThrowAgain = False
        self.sixesThrown = 0
        self.someoneWon = False
        self.numPlayers = len(self.players)
        self.printResults = False
        self.playerColors = {0: 'yellow', 1: 'blue', 2: 'red', 3: 'green'}
        
    def simGame(self):
        capture = False
        turn = self.throwDiceForStart()
    
        while not(self.someoneWon):
            if not capture:
                stepsForward = self.determineStepsForward()
            else:
                stepsForward = 20
            
            capture = self.makeMove(turn, stepsForward)
            
            self.someoneWon = (len(self.players[turn].pawns) == 0)
            if self.someoneWon:
                self.winner = turn
            
            if not(capture) and not(self.canThrowAgain):
                turn += 1
                self.steps += 1
                if turn >= self.numPlayers:
                    turn = 0
                self.sixesThrown = 0
            self.canThrowAgain = False
    
    def makeMove(self, i, stepsForward):
        capture = False
        pawnsToMove = self.players[i].findPawnsToMove(self.board, stepsForward)
        if self.printResults:
            print('pawns to move:', pawnsToMove)
        if pawnsToMove:
            if self.players[i].strategy == 'player': # should only exist in player played game, should check for object GamePlayer
                pawn = self.playerPickMove(i, stepsForward, pawnsToMove) # draw virtual moves and let the player pick a move
            else:
                if len(pawnsToMove) == 1: # or at the same pos
                    pawn = pawnsToMove[0]
                else:
                    pawn = self.players[i].performStrategy(self.players, self.board, pawnsToMove, stepsForward) # move in head
            if self.printResults:
                print('will move:', pawn)        
            positions = self.players[i].findNewPos(pawn, stepsForward) # move in head
            if self.sixesThrown == 3 and positions[1] < self.board.boardSize: # remove only if it didn't land in the end zone
                self.players[i].makeMove(pawn, -1, self.board.boardSize)
                self.board.makeMove(self.players, i, pawn, positions[0], -1) # can only remove if it is on the board
            else:
                self.players[i].makeMove(pawn, positions[1], self.board.boardSize) # move in head
                capture = self.board.capturePawn(self.players, i, positions[1])
                self.board.makeMove(self.players, i, pawn, positions[0], positions[1]) # move in real life
        self.someoneWon = (len(self.players[i].pawns) == 0) # not(self.pawns)
        
        return(capture)
    
    def determineStepsForward(self): # should add +7 if all pawns are on table
        diceNumber = randrange(1,7)
        if diceNumber == 6:
            self.canThrowAgain = True
            self.sixesThrown += 1
            if self.sixesThrown == 3:
                self.canThrowAgain = False
        else:
            self.canThrowAgain = False
    
        return(diceNumber)
        
    def throwDiceForStart(self):
        thrownNumbers = [[i,0] for i in range(self.numPlayers)]

        while len(thrownNumbers) > 1:
            for i, thrownNumber in enumerate(thrownNumbers):
                thrownNumber[1] = randrange(1,7)
                if self.printResults:
                    print(self.playerColors[thrownNumber[0]], 'rolled', thrownNumber[1])  
            highestDice = max([elem[1] for elem in thrownNumbers])
            thrownNumbers = [[num, dice] for num, dice in thrownNumbers if dice == highestDice]
            
        if self.printResults:
            print(self.playerColors[thrownNumbers[0][0]], 'starts the game')

        return(thrownNumbers[0][0])       


class GamePlayer(Game): # plays one game
    def __init__(self, strategies):
        super().__init__(strategies)
        self.printResults = True
        self.W = 800
        self.H = 800
        pygame.init()
        self.screen = pygame.display.set_mode((self.W, self.H))
        drawBoard(self.screen, self.W, self.H)
        self.screen_copy = self.screen.copy()
        drawPawnsAtHome(self.screen, self.players)
        
    def playGame(self): # plays one game
        t = self.throwDiceForStart()
        capture = False
        
        while not(self.someoneWon):
            nextStep = False
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYUP:
                    if event.key == K_SPACE or event.key == K_RETURN:
                        nextStep = True
            
            pygame.display.update()
            
            if nextStep:
                if capture:
                    stepsForward = 20
                else:    
                    stepsForward = self.determineStepsForward()
                
                print(self.board.filledBoard)
                print(self.playerColors[t], 'can move:', stepsForward)
                capture = self.makeMove(t, stepsForward)
                
                if self.someoneWon:
                    self.winner = self.players[t].name
                    print(self.players[t].name, 'HAS WON!!!')
                
                if not(capture) and not(self.canThrowAgain):
                    t += 1
                    self.steps += 1
                    if t >= self.numPlayers:
                        t = 0
                    self.sixesThrown = 0
                if self.canThrowAgain:
                    self.canThrowAgain = False
                
                # redraw:
                self.screen.blit(self.screen_copy, (0,0))
                drawPawnsOnBoard(self.screen, self.board.filledBoard)
                drawPawnsAtHome(self.screen, self.players)
                drawPawnsAtFinishline(self.screen, self.board.filledFinishLine)
                drawFinishedPawns(self.screen, self.players)
             
    def playerPickMove(self, t, stepsForward, pawnsToMove):
        finishedVirtual = []
        virtualBoard = copy.deepcopy(self.board)
        for i, pawnToMove in enumerate(pawnsToMove):
            positions = self.players[t].findNewPos(pawnToMove, stepsForward)
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
        self.screen.blit(self.screen_copy, (0,0))
        drawPawnsOnBoard(self.screen, virtualBoard.filledBoard)
        drawPawnsAtHome(self.screen, self.players)
        drawPawnsAtFinishline(self.screen, virtualBoard.filledFinishLine)
        drawFinishedPawns(self.screen, self.players)
        drawFinishedVirtualMoves(self.screen, self.players, t, finishedVirtual)
        pygame.display.update()
        
        key1 = False
        key2 = False
        key3 = False
        key4 = False
        pawnNumber = False
        def getPawnNumber(numberOfOptions, numberPressed): # helper function
            pawnNumber = False
            for i in range(numberOfOptions):
                if numberPressed[i] == True:
                    pawnNumber = i + 1
            return(pawnNumber)
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
            
        return(pawnsToMove[pawnNumber-1])
        