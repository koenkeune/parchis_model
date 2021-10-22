import sys
from random import shuffle
from board import *
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
    gameInst = game(strategies)
    gameInst.playGame()
else:
    strategies = ['safest', 'safest', 'furthest', 'furthest']
    winners = {}
    for i in range(4):
        winners[strategies[i]] = 0
        
    for i in range(runs):
        board = Board()
        shuffle(strategies) # the order of the players is randomized
        gameInst = game(strategies)
        gameInst.simGame()
        winners[gameInst.players[gameInst.winner].strategy] += 1

    if runs == 1:
        print(gameInst.board.filledBoard)
        print(gameInst.players[gameInst.winner].name, 'with strategy', gameInst.players[gameInst.winner].strategy, 'won in', gameInst.steps, 'steps')
    else:
        allStrategies = set(strategies)
        strategiesRepeats = {} # correct for repeated strategies in game
        for strategy in strategies:
            if strategy in strategiesRepeats:
                strategiesRepeats[strategy] += 1
            else:
                strategiesRepeats[strategy] = 1
            
        for strategy in allStrategies:
            print('stategy', strategy, 'won:', (winners[strategy] / runs / strategiesRepeats[strategy]) * 100, '% of the games')
      
      

