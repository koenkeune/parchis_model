from random import randrange

# updating part 
    
def game(board, players):
    # while...
    print(board)
    sixesThrown = 0
    # for each player...
    diceNumber = randrange(1,7)
    if diceNumber == 6 & sixesThrown == 2:
        print('pass') # pass
    elif diceNumber == 6:
        sixesThrown += 1
        
    board = players[0].makeMove(board, sixesThrown)
    
        
    print(players[0].pawns)
    print(players[1].pawns)
        
    print(board)
    
 
    
    
