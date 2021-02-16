import sys
from board import *
from game import *

if len(sys.argv) - 1 > 1:
    sys.exit("first argument is optional and is the number of runs")
elif len(sys.argv) - 1 == 1:
    runs = sys.argv[1]
else:
    runs = 1

winners = {}
for i in range(4):
    winners[i] = 0
    
for i in range(runs):
    board = Board(68)
    players = list()
    players.append(Player(0, board.boardSize, 'safest'))
    for j in range(1,4):
        players.append(Player(j, board.boardSize, 'furthest'))
    result = game(board, players)
    winners[int(result[1][6])] += 1

if runs == 1:
    print(result[0])
    print(result[1], 'WON! in', result[2], 'steps')
else:
    for i in range(4):
        print('player', i, 'won:', (winners[i] / runs) * 100, '% of the games')

