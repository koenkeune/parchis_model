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
            diceNumber = 6 # every player start with a 'free' turn
            while diceNumber == 6 and not(someoneWon):
                diceNumber = randrange(1,7)
                print(diceNumber)
                if diceNumber == 6:
                    sixesThrown += 1

                pawnsToMove = players[i].findPawnsToMove(diceNumber)

                if pawnsToMove:
                    pawn = players[i].findFurthestPawn(pawnsToMove)
                    positions = players[i].findNewPos(pawn, diceNumber)
                    players[i].makeMove(pawn, positions[1], board.boardSize)
                    board.makeMove(players, i, pawn, positions[0], positions[1])
                    
                if sixesThrown == 3:
                    diceNumber = 0 # a number to get out of the while loop
                    if pawnsToMove:
                        if positions[1] < board.boardSize: # remove only if it didn't land in the end zone
                            players[i].makeMove(pawn, -1, board.boardSize)
                            board.makeMove(players, i, pawn, positions[1], -1)
                    
                someoneWon = (len(players[i].pawns) == 0) # not(self.pawns)
                
            if someoneWon:
                print(players[i].name, ' WON!')
                print('in ', j, ' steps')
            i += 1
            
    print(board.filledBoard)
    
 
    
    
