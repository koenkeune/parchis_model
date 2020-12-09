from random import randrange

# updating part 
    
def game(board, players):
    # while...
    print(board.filledBoard)
    someoneWon = False
    for i in range(100):
        for player in players:
            sixesThrown = 0
            diceNumber = 6 # every player start with a 'free' turn
            while (diceNumber == 6) and (sixesThrown < 3) and not(someoneWon):
                diceNumber = randrange(1,7)
                if diceNumber == 6:
                    sixesThrown += 1
                movedPawn = player.makeMove(diceNumber, board.boardSize)
                board.makeMoveOnBoard(player, movedPawn[0], movedPawn[1], movedPawn[2])
                someoneWon = (len(player.pawns) == 0)
            
        if someoneWon:
            print(player.name, ' WON!')
        
        
    print(board.filledBoard)
    
 
    
    
