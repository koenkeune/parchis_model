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
        
    def check_rule3_case1(self):
        pl = 2
        self.game.board.filledBoard = self.scenes.Test3_case1.BOARD
        self.game.players[pl].pawns = self.scenes.Test3_case1.PLAYER2PAWNS
        self.game.players[pl].pawnsHome = self.scenes.Test3_case1.PLAYER2PAWNSHOME
        self.game.players[pl].pawnsFinished = self.scenes.Test3_case1.PLAYER2PAWNSFINISHED
        diceNumber = 2
        self.game.playOneThrow(pl, diceNumber)
        
        return(self.game.board.filledBoard == self.scenes.Test3_case1.BOARDAFTER)
        
    def check_rule3_case2(self): # two captures in a row
        pl = 2
        self.game.board.filledBoard = self.scenes.Test3_case2.BOARD
        self.game.players[pl].pawns = self.scenes.Test3_case2.PLAYER2PAWNS
        self.game.players[pl].pawnsHome = self.scenes.Test3_case2.PLAYER2PAWNSHOME
        self.game.players[pl].pawnsFinished = self.scenes.Test3_case2.PLAYER2PAWNSFINISHED
        diceNumber = 2
        self.game.playOneThrow(pl, diceNumber)
        
        return(self.game.board.filledBoard == self.scenes.Test3_case2.BOARDAFTER)    
        
    def check_rule4(self):
        pl = 0 # turn of player
        self.game.board.filledBoard = self.scenes.Test4.BOARD
        self.game.players[pl].pawns = self.scenes.Test4.PLAYER0PAWNS
        self.game.players[pl].pawnsHome = self.scenes.Test4.PLAYER0PAWNSHOME
        self.game.players[pl].pawnsFinished = self.scenes.Test4.PLAYER0PAWNSFINISHED
        diceNumber = 5
        self.game.makeMove(pl, diceNumber)
        
        return(self.game.board.filledBoard == self.scenes.Test4.BOARDAFTER)
        
    def check_rule4_1a(self):
        pl = 1
        self.game.board.filledBoard = self.scenes.Test4_1a.BOARD
        self.game.players[pl].pawns = self.scenes.Test4_1a.PLAYER1PAWNS
        self.game.players[pl].pawnsHome = self.scenes.Test4_1a.PLAYER1PAWNSHOME
        self.game.players[pl].pawnsFinished = self.scenes.Test4_1a.PLAYER1PAWNSFINISHED
        self.game.players[pl].strategy = 'furthest'
        diceNumber = 5
        self.game.makeMove(pl, diceNumber)
        
        return(self.game.board.filledBoard == self.scenes.Test4_1a.BOARDAFTER)
        
    def check_rule4_1b(self):
        pl = 1
        self.game.board.filledBoard = self.scenes.Test4_1b.BOARD
        self.game.players[pl].pawns = self.scenes.Test4_1b.PLAYER1PAWNS
        self.game.players[pl].pawnsHome = self.scenes.Test4_1b.PLAYER1PAWNSHOME
        self.game.players[pl].pawnsFinished = self.scenes.Test4_1b.PLAYER1PAWNSFINISHED
        self.game.players[pl].strategy = 'furthest'
        diceNumber = 5
        self.game.makeMove(pl, diceNumber)
        
        return(self.game.board.filledBoard == self.scenes.Test4_1b.BOARDAFTER)
        
    def check_rule4_2(self):
        pl = 2
        self.game.board.filledBoard = self.scenes.Test4_2.BOARD
        self.game.players[pl].pawns = self.scenes.Test4_2.PLAYER2PAWNS
        self.game.players[pl].pawnsHome = self.scenes.Test4_2.PLAYER2PAWNSHOME
        self.game.players[pl].pawnsFinished = self.scenes.Test4_2.PLAYER2PAWNSFINISHED
        self.game.players[pl].strategy = 'furthest'
        diceNumber = 5
        self.game.playOneThrow(pl, diceNumber)
        
        return(self.game.board.filledBoard == self.scenes.Test4_2.BOARDAFTER)
