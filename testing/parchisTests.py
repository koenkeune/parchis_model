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
        
    def check_rule2(self, diceNumber):
        pl = 0
        self.game.board.filledBoard = copy.deepcopy(self.scenes.Test2.BOARD) # deepcopy to be able to run it multiple times
        self.game.players[pl].pawns = copy.deepcopy(self.scenes.Test2.PLAYER0PAWNS)
        self.game.players[pl].pawnsHome = self.scenes.Test2.PLAYER0PAWNSHOME
        self.game.players[pl].pawnsFinished = self.scenes.Test2.PLAYER0PAWNSFINISHED
        self.game.makeMove(pl, diceNumber)
        
        return(self.game.board.filledBoard == self.scenes.Test2.BOARDAFTER) # true for dicenumbers larger than 1
        
    def check_rule2_1(self): # can't pass through own bridge also tested
        pl = 3
        self.game.board.filledBoard = self.scenes.Test2_1.BOARD
        self.game.players[pl].pawns = self.scenes.Test2_1.PLAYER0PAWNS
        self.game.players[pl].pawnsHome = self.scenes.Test2_1.PLAYER0PAWNSHOME
        self.game.players[pl].pawnsFinished = self.scenes.Test2_1.PLAYER0PAWNSFINISHED
        diceNumber = 3
        self.game.makeMove(pl, diceNumber)
        
        return(self.game.board.filledBoard == self.scenes.Test2_1.BOARDAFTER)
        
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

    def check_rule5(self):
        pl = 0 # turn of player
        self.game.board.filledBoard = self.scenes.Test5.BOARD
        self.game.players[pl].pawns = self.scenes.Test5.PLAYER0PAWNS
        self.game.players[pl].pawnsHome = self.scenes.Test5.PLAYER0PAWNSHOME
        self.game.players[pl].pawnsFinished = self.scenes.Test5.PLAYER0PAWNSFINISHED
        diceNumbers = [6, 3]
        self.game.playOneTurn(pl, diceNumbers)
        
        return(self.game.board.filledBoard == self.scenes.Test5.BOARDAFTER)
        
    def check_rule5_1(self):
        pl = 0
        self.game.players[pl].pawnsHome = 0
        
        return(self.game.determineStepsForward(pl, 6) == 7)    
        
    def check_rule5_2(self):
        pl = 0 # turn of player
        self.game.board.filledBoard = self.scenes.Test5_2.BOARD
        self.game.players[pl].pawns = self.scenes.Test5_2.PLAYER0PAWNS
        self.game.players[pl].pawnsHome = self.scenes.Test5_2.PLAYER0PAWNSHOME
        self.game.players[pl].pawnsFinished = self.scenes.Test5_2.PLAYER0PAWNSFINISHED
        self.game.players[pl].strategy = 'furthest'
        diceNumbers = [6, 1]
        self.game.playOneTurn(pl, diceNumbers)
        
        return(self.game.board.filledBoard == self.scenes.Test5_2.BOARDAFTER)        
        
    def check_rule5_3(self):
        pl = 0 # turn of player
        self.game.board.filledBoard = self.scenes.Test5_3.BOARD
        self.game.players[pl].pawns = self.scenes.Test5_3.PLAYER0PAWNS
        self.game.players[pl].pawnsHome = self.scenes.Test5_3.PLAYER0PAWNSHOME
        self.game.players[pl].pawnsFinished = self.scenes.Test5_3.PLAYER0PAWNSFINISHED
        diceNumbers = [6, 6, 6]
        self.game.playOneTurn(pl, diceNumbers)
        
        return(self.game.board.filledBoard == self.scenes.Test5_3.BOARDAFTER)

    def check_rule5_3a_case1(self): # boundary test 1
        pl = 0 # turn of player
        self.game.board.filledBoard = self.scenes.Test5_3a_case1.BOARD
        self.game.board.filledFinishLine = self.scenes.Test5_3a_case1.FINISHLINE
        self.game.players[pl].pawns = self.scenes.Test5_3a_case1.PLAYER0PAWNS
        self.game.players[pl].pawnsHome = self.scenes.Test5_3a_case1.PLAYER0PAWNSHOME
        self.game.players[pl].pawnsFinished = self.scenes.Test5_3a_case1.PLAYER0PAWNSFINISHED
        self.game.sixesThrown = 0
        diceNumbers = [6, 6, 6]
        self.game.playOneTurn(pl, diceNumbers)
        
        return(self.game.board.filledBoard == self.scenes.Test5_3a_case1.BOARDAFTER and 
            self.game.board.filledFinishLine == self.scenes.Test5_3a_case1.FINISHLINEAFTER)
        
    def check_rule5_3a_case2(self): # boundary test 2
        pl = 0 # turn of player
        self.game.board.filledBoard = self.scenes.Test5_3a_case2.BOARD
        self.game.board.filledFinishLine = self.scenes.Test5_3a_case2.FINISHLINE
        self.game.players[pl].pawns = self.scenes.Test5_3a_case2.PLAYER0PAWNS
        self.game.players[pl].pawnsHome = self.scenes.Test5_3a_case2.PLAYER0PAWNSHOME
        self.game.players[pl].pawnsFinished = self.scenes.Test5_3a_case2.PLAYER0PAWNSFINISHED
        self.game.sixesThrown = 0
        diceNumbers = [6, 6, 6]
        self.game.playOneTurn(pl, diceNumbers)
        
        return(self.game.board.filledBoard == self.scenes.Test5_3a_case2.BOARDAFTER and 
            self.game.board.filledFinishLine == self.scenes.Test5_3a_case2.FINISHLINEAFTER)    
