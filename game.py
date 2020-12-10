from random import randrange

# updating part 
    
def game(board, players):
    # while...
    print(board.filledBoard)
    someoneWon = False
    numPlayers = len(players)
    while not(someoneWon):
        i = 0
        while not(someoneWon) and i < numPlayers:
            sixesThrown = 0
            diceNumber = 6 # every player start with a 'free' turn
            while diceNumber == 6 and not(someoneWon):
                diceNumber = randrange(1,7)
                if diceNumber == 6:
                    sixesThrown += 1
                movedPawn = players[i].moveFurthestPawn(diceNumber)
                
                players[i].makeMove(movedPawn[0], movedPawn[2], board.boardSize)
                board.makeMoveOnBoard(players[i], movedPawn[0], movedPawn[1], movedPawn[2])
                
                someoneWon = (len(players[i].pawns) == 0)
                if sixesThrown == 3:
                    players[i].makeMove(movedPawn[0], -1, board.boardSize)
                    board.makeMoveOnBoard(players[i], movedPawn[0], movedPawn[2], -1)
                    diceNumber = 0 # a number to get out of the while loop
            if someoneWon:
                print(players[i].name, ' WON!')
            i += 1
        
        
    print(board.filledBoard)
    
 
    
    
