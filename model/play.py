import sys
from random import shuffle
from game import *

play = False
if len(sys.argv) - 1 > 1:
    sys.exit("first argument is optional and is the number of runs")
elif len(sys.argv) - 1 == 1:
    runs = int(sys.argv[1])
else:
    play = True

if play:
    strategies = ['player', 'safest', 'furthest', 'furthest']
    GamePlayer(strategies).playGame()
else:
    strategies = ['safest', 'safest', 'furthest', 'safest']
    winners = {}
    for i in range(4):
        winners[strategies[i]] = 0
        
    for i in range(runs):
        shuffle(strategies) # the order of the players is randomized
        gamePlayed = Game(strategies)
        gamePlayed.simGame()
        winners[gamePlayed.players[gamePlayed.winner].strategy] += 1

    if runs == 1:
        print(gamePlayed.board.filledBoard)
        print(gamePlayed.players[gamePlayed.winner].name, 'with strategy', gamePlayed.players[gamePlayed.winner].strategy, 'won in', gamePlayed.steps, 'steps')
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