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
                            players[i].makeMove(pawn, positions[1], board.boardSize) # move in head
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
    screen_copy = screen.copy()
    # draw pawns at home
    for player in players:
        for i in range(player.pawnsHome):
            drawPawn(-1, player.number, screen, 0, i, 0, False)
    
    winner = 'no one'
    someoneWon = False
    numPlayers = len(players)
    t = 0 # turn
    sixesThrown = 0
    capture = False
    canThrowAgain = False
    
    while True:
        keyPressed = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYUP:
                keyPressed = True
        
        pygame.display.update()
        
        if keyPressed:
            if t >= numPlayers:
                t = 0
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
            
            print(board.filledBoard)
            print(getPlayerColorString(t), 'can move:', stepsForward)
            
            # repeat if capture
            pawnsToMove = players[t].findPawnsToMove(board, stepsForward)
            print('pawns to move:', pawnsToMove)
            if pawnsToMove:
                if len(pawnsToMove) == 1: # or at the same pos
                    pawn = pawnsToMove[0]
                else:
                    pawn = players[t].performStrategy(players, board, pawnsToMove, t, stepsForward) # move in head
                print('will move:', pawn)
                positions = players[t].findNewPos(pawn, stepsForward) # move in head
                if sixesThrown == 3 and positions[1] < board.boardSize: # remove only if it didn't land in the end zone
                    players[t].makeMove(pawn, -1, board.boardSize)
                    board.makeMove(players, t, pawn, positions[0], -1) # can only remove if it is on the board
                else:
                    players[t].makeMove(pawn, positions[1], board.boardSize) # move in head
                    capture = board.capturePawn(players, t, positions[1])
                    board.makeMove(players, t, pawn, positions[0], positions[1]) # move in real life
                    if capture:
                        stepsForward = 20
                        
            # someoneWon = (len(players[t].pawns) == 0) # not(self.pawns)
            # if someoneWon:
                # winner = players[t].name
            
            print('capture', capture, 'canThrowAgain', canThrowAgain)
            
            if not(capture) and not(canThrowAgain):
                t += 1
                sixesThrown = 0
            if canThrowAgain:
                canThrowAgain = False    
            
            ### redraw:
            screen.blit(screen_copy, (0,0))        
            # draw board
            pawnSpots = [board.filledBoard.index(spot) for spot in board.filledBoard if spot]
            for pawnSpot in pawnSpots:
                twoPawns = 0
                if len(board.filledBoard[pawnSpot]) == 2:
                    twoPawns = 1
                for pawn in board.filledBoard[pawnSpot]:
                    drawPawn(pawnSpot, int(pawn[6]), screen, twoPawns, 0, 0, False)
                    twoPawns += 1
            # draw pawns at home
            for player in players:
                for i in range(player.pawnsHome):
                    drawPawn(-1, player.number, screen, 0, i, 0, False)
            # draw pawns at finish line
            for i in range(4):
                pawnSpots = [board.filledFinishLine[i].index(spot) for spot in board.filledFinishLine[i] if spot]
                for pawnSpot in pawnSpots:
                    twoPawns = 0
                    if len(board.filledFinishLine[i][pawnSpot]) == 2:
                        twoPawns = 1
                    for pawn in board.filledFinishLine[i][pawnSpot]:
                        drawPawn(pawnSpot, int(pawn[6]), screen, twoPawns, 0, 0, True)
                        twoPawns += 1
            # draw finished pawns
            for i in range(4):
                for j in range(players[i].pawnsFinished):
                    drawPawn(0, i, screen, 0, 0, j + 1, False)
            ###
                
def getPlayerColorString(playerNum):
    if playerNum == 0:
        return('yellow')
    elif playerNum == 1:
        return('blue')
    elif playerNum == 2:
        return('RED')
    elif playerNum == 3:
        return('GREEN')
    
