from random import randrange
from visualizer import *
import pygame, sys
from pygame.locals import *
    
# runs one game according to the rules    
def game(board, players):
    winner = 'no one'
    someoneWon = False
    numPlayers = len(players)
    j = 0
    while not(someoneWon):
        i = 0
        j += 1
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
                    pawnsToMove = players[i].findPawnsToMove(board, stepsForward)
                    if pawnsToMove:
                        if len(pawnsToMove) == 1: # or at the same pos
                            pawn = pawnsToMove[0]
                        else:
                            pawn = players[i].performStrategy(players, board, pawnsToMove, i, stepsForward) # move in head
                        positions = players[i].findNewPos(pawn, stepsForward) # move in head
                        if sixesThrown == 3 and positions[1] < board.boardSize: # remove only if it didn't land in the end zone
                            players[i].makeMove(pawn, -1, board.boardSize)
                            board.makeMove(players, i, pawn, positions[0], -1) # can only remove if it is on the board
                        else:
                            players[i].makeMove(pawn, positions[1], board.boardSize) # move in real life
                            capture = board.capturePawn(players, i, positions[1])
                            board.makeMove(players, i, pawn, positions[0], positions[1]) # move in real life
                            if capture:
                                stepsForward = 20
                if sixesThrown == 3:
                    diceNumber = 0 # a number to get out of the while loop 
                someoneWon = (len(players[i].pawns) == 0) # not(self.pawns)
            if someoneWon:
                winner = players[i].name
            i += 1
    
    return(board.filledBoard, winner, j)
    
def gameVis(board, players):
    pygame.init()
    W = 900
    H = 900
    screen = pygame.display.set_mode((W, H))
    drawBoard(screen, W, H)
    
    for player in players:
        i = 0
        for pawn in player.pawns:
            drawPawn(player.pawns[pawn], player.number, screen, W, H, i)
            i += 1
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
    
