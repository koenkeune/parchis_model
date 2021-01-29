from random import randrange

# updating part 
    
def game(board, players):
    print(board.filledBoard)
    someoneWon = False
    numPlayers = len(players)
    j = 0
    while not(someoneWon):
        i = 0
        j += 1
        print(board.filledBoard)
        while not(someoneWon) and i < numPlayers:
            sixesThrown = 0
            diceNumber = 6 # to get in the while
            while diceNumber == 6 and not(someoneWon):
                diceNumber = randrange(1,7)
                print(diceNumber)
                if diceNumber == 6:
                    sixesThrown += 1
                stepsForward = diceNumber
                capture = True
                while capture:
                    capture = False
                    pawnsToMove = players[i].findPawnsToMove(board, stepsForward)

                    if pawnsToMove:
                        pawn = players[i].findFurthestPawn(pawnsToMove) # move in head
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
                print(players[i].name, ' WON!')
                print('in ', j, ' steps')
            i += 1
            
    print(board.filledBoard)
    
 
    
    
