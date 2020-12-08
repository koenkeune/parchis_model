from random import randrange

# updating part 
    
def game(board, players):
    # while...
    print(board.filledBoard)
    sixesThrown = 0
    # for each player...
    for player in players:
        diceNumber = randrange(1,7)
        if diceNumber == 6 & sixesThrown == 2:
            print('pass') # pass
        elif diceNumber == 6:
            sixesThrown += 1
        
        print('diceNumber: ')
        print(diceNumber)
            
        movedPawn = player.makeMove(diceNumber, board.boardSize)
        board.makeMoveOnBoard(player, movedPawn[0], movedPawn[1], movedPawn[2])
        
    print(player.pawns)
        
    print(board.filledBoard)
    
 
    
    
