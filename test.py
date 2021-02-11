# import sys
from board import *
from game import *

# if len(sys.argv) - 1 != 2:
    # sys.exit("number of arguments should be 2")
# else:
    # numberOfPlayers = sys.argv[1]
    # boardSize = sys.argv[2]

# if boardSize == "big":
    # boardSize = 102
# elif (boardSize == "small"):
    # boardSize = 68
# else:
    # sys.exit("incorrect boardsize either small or large")

winners = {}
for i in range(4):
    winners[i] = 0
    
runs = 1000
for i in range(runs):
    board = Board(68)
    players = list()
    players.append(Player(0, board.boardSize, 'safest'))
    for j in range(1,4):
        players.append(Player(j, board.boardSize, 'furthest'))
    result = game(board, players)
    winners[int(result[1][6])] += 1
    
for i in range(4):
    print('player', i, 'won:', (winners[i] / runs) * 100, '% of the games')

