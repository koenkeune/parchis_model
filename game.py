from random import randrange

# updating part 
    
def game(board, players):
    # while...
    sixesThrown = 0
    # for each player...
    diceNumber = players[0].makeMove()
    if diceNumber == 6 & sixesThrown == 2:
        print('pass') # pass
    elif diceNumber == 6:
        sixesThrown += 1
        
    print(players[0].pawns)
    print(players[1].pawns)
        
        
    
 
    
    
