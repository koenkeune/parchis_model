from random import randrange

# updating part 
    
def game(board, players):
    # while...
    print(board.filledBoard)
    sixesThrown = 0
    # for each player...
    diceNumber = randrange(1,7)
    if diceNumber == 6 & sixesThrown == 2:
        print('pass') # pass
    elif diceNumber == 6:
        sixesThrown += 1
    
    print('diceNumber: ')
    print(diceNumber)    
        
    players[0].makeMove(diceNumber, board.boardSize)
    
        
    print(players[0].pawns)
    print(players[1].pawns)
        
    print(board.filledBoard)
    
 
    
    
