from model.game import *
from scenarios import *
import copy

class RulesTester():
    def __init__(self, game):
        self.game = game
        self.scenes = Scenarios()
        
    def check_rule1(self):
        numPlayers = len(self.game.players)
        starts = []
        for i in range(100):
            starts.append(self.game.throwDiceForStart())
            
        return(len(set(starts)) == numPlayers)
        
    def check_rule4(self):
        pl = 0 # turn of player
        self.game.board.filledBoard = self.scenes.TEST1BOARD
        self.game.players[pl].pawns = self.scenes.TEST1PLAYER0PAWNS
        self.game.players[pl].pawnsHome = self.scenes.TEST1PLAYER0PAWNSHOME
        self.game.players[pl].pawnsFinished = self.scenes.TEST1PLAYER0PAWNSFINISHED
        diceNumber = 5
        self.game.makeMove(pl, diceNumber)
        pawnsAtHome = 1
        
        return(self.game.board.filledBoard == self.scenes.TEST1BOARDAFTER)
        
    def check_rule4a(self):
        pl = 1
        self.game.board.filledBoard = self.scenes.TEST2BOARD
        self.game.players[pl].pawns = self.scenes.TEST2PLAYER1PAWNS
        self.game.players[pl].pawnsHome = self.scenes.TEST2PLAYER1PAWNSHOME
        self.game.players[pl].pawnsFinished = self.scenes.TEST2PLAYER1PAWNSFINISHED
        self.game.players[pl].strategy = 'furthest'
        diceNumber = 5
        self.game.makeMove(pl, diceNumber)
        pawnsAtHome = 1
        
        return(self.game.board.filledBoard == self.scenes.TEST2BOARDAFTER)