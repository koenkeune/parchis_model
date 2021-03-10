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
    players = list()
    board = Board()
    players.append(Player(0, board.boardSize, 'player'))
    players.append(Player(1, board.boardSize, 'safest'))
    players.append(Player(2, board.boardSize, 'furthest'))
    players.append(Player(3, board.boardSize, 'furthest'))
    # for j in range(2,4):
        # players.append(Player(j, board.boardSize, 'furthest'))
    result = gameVis(board, players)
else:
    strategies = ['safest', 'safest', 'furthest', 'furthest']
    winners = {}
    for i in range(4):
        winners[strategies[i]] = 0
        
    for i in range(runs):
        board = Board()
        players = list()
        shuffle(strategies) # the order of the players is randomized
        for j in range(4):
            players.append(Player(j, board.boardSize, strategies[j]))
        result = game(board, players)
        winners[result[2]] += 1

    if runs == 1:
        print(result[0])
        print(result[1], 'with strategy', result[2], 'won in', result[3], 'steps')
    else:
        allStrategies = set(strategies)
        for strategy in allStrategies:
            print('stategy', strategy, 'won:', (winners[strategy] / runs) * 100, '% of the games')

