import sys
from game import *

play = False
debug = False
try:
    if len(sys.argv) - 1 > 1:
        sys.exit("First argument is optional and is the number of runs")
    elif len(sys.argv) - 1 == 1:
        if sys.argv[1] == 'debug':
            debug = True
            play = True
        else:    
            runs = int(sys.argv[1])
    else:
        play = True
except ValueError:
    sys.exit("Run the model with python model/play.py [runs]\nTest the model with python testing/test.py")

if play:
    # how many players?
    numPlayers = 0
    while numPlayers < 1 or numPlayers > 4:
        input_value = input("With how many players do you want to play? ")
        try:
            if int(input_value) < 1 or int(input_value) > 4:
                print("please select a number between 1 and 4".format(input=input_value))  
            numPlayers = int(input_value)
        except ValueError:
            print("{input} is not a number, please enter a number only".format(input=input_value))     
    
    strategies = ['player', 'safest', 'furthest', 'furthest']
    if numPlayers == 2:
        strategies = ['player', 'safest', 'player', 'furthest']
    elif numPlayers == 3:
        strategies = ['player', 'player', 'player', 'furthest']
    elif numPlayers == 4:
        strategies = ['player', 'player', 'player', 'player']
    GamePlayer(strategies, debug).playGame()
else:
    strategies = ['safest', 'agressive', 'safest', 'agressive']
    winners = {}
    for i in range(4):
        winners[strategies[i]] = 0
        
    for i in range(runs):
        gamePlayed = Game(strategies)
        gamePlayed.simGame()
        winners[gamePlayed.players[gamePlayed.winner].strategy] += 1

    if runs == 1:
        print(gamePlayed.board.filledBoard)
        print(gamePlayed.players[gamePlayed.winner].name, 'with strategy', gamePlayed.players[gamePlayed.winner].strategy, 'won in', gamePlayed.totalTurns, 'turns')
    else:
        allStrategies = set(strategies)
        # strategiesRepeats = {} # correct for repeated strategies in game
        # for strategy in strategies:
            # if strategy in strategiesRepeats:
                # strategiesRepeats[strategy] += 1
            # else:
                # strategiesRepeats[strategy] = 1
            
        for strategy in allStrategies:
            print('stategy', strategy, 'won:', (winners[strategy] / runs) * 100, '% of the games')