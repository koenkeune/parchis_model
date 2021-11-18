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
        
    def check_rule2_case1(self, diceNumber):
        pl = 0
        self.game.board.filledBoard = copy.deepcopy(self.scenes.Test2_case1.BOARD) # deepcopy to be able to run it multiple times
        self.game.players[pl].pawns = copy.deepcopy(self.scenes.Test2_case1.PLAYER0PAWNS)
        self.game.players[pl].pawnsHome = self.scenes.Test2_case1.PLAYER0PAWNSHOME
        self.game.players[pl].pawnsFinished = self.scenes.Test2_case1.PLAYER0PAWNSFINISHED
        self.game.makeMove(pl, diceNumber)
        
        return(self.game.board.filledBoard == self.scenes.Test2_case1.BOARDAFTER) # true for dicenumbers larger than 1
        
    def check_rule2_case2(self): 
        pl = 3
        self.game.board.filledBoard = self.scenes.Test2_case2.BOARD
        self.game.players[pl].pawns = self.scenes.Test2_case2.PLAYER3PAWNS
        self.game.players[pl].pawnsHome = self.scenes.Test2_case2.PLAYER3PAWNSHOME
        self.game.players[pl].pawnsFinished = self.scenes.Test2_case2.PLAYER3PAWNSFINISHED
        diceNumber = 3
        self.game.makeMove(pl, diceNumber)
        
        return(self.game.board.filledBoard == self.scenes.Test2_case2.BOARDAFTER)
        
    def check_rule2_case3(self): # can't pass through own bridge
        pl = 3
        self.game.board.filledBoard = self.scenes.Test2_case3.BOARD
        self.game.players[pl].pawns = self.scenes.Test2_case3.PLAYER3PAWNS
        self.game.players[pl].pawnsHome = self.scenes.Test2_case3.PLAYER3PAWNSHOME
        self.game.players[pl].pawnsFinished = self.scenes.Test2_case3.PLAYER3PAWNSFINISHED
        diceNumber = 2
        self.game.makeMove(pl, diceNumber)
        
        return(self.game.board.filledBoard == self.scenes.Test2_case3.BOARDAFTER)    
        
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
        
    def check_rule5_2_case1(self):
        pl = 0 # turn of player
        self.game.board.filledBoard = self.scenes.Test5_2_case1.BOARD
        self.game.players[pl].pawns = self.scenes.Test5_2_case1.PLAYER0PAWNS
        self.game.players[pl].pawnsHome = self.scenes.Test5_2_case1.PLAYER0PAWNSHOME
        self.game.players[pl].pawnsFinished = self.scenes.Test5_2_case1.PLAYER0PAWNSFINISHED
        self.game.players[pl].strategy = 'furthest'
        diceNumbers = [6, 1]
        self.game.playOneTurn(pl, diceNumbers)
        
        return(self.game.board.filledBoard == self.scenes.Test5_2_case1.BOARDAFTER)
        
    def check_rule5_2_case2(self):
        pl = 0 # turn of player
        self.game.board.filledBoard = self.scenes.Test5_2_case2.BOARD
        self.game.players[pl].pawns = self.scenes.Test5_2_case2.PLAYER0PAWNS
        self.game.players[pl].pawnsHome = self.scenes.Test5_2_case2.PLAYER0PAWNSHOME
        self.game.players[pl].pawnsFinished = self.scenes.Test5_2_case2.PLAYER0PAWNSFINISHED
        self.game.players[pl].strategy = 'furthest'
        diceNumbers = [6, 1]
        self.game.playOneTurn(pl, diceNumbers)
        
        return(self.game.board.filledBoard == self.scenes.Test5_2_case2.BOARDAFTER)     
        
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

    def check_rule6(self, diceNumber):
        pl = 0 # turn of player
        self.game.board.filledBoard = copy.deepcopy(self.scenes.Test6.BOARD)
        self.game.board.filledFinishLine = copy.deepcopy(self.scenes.Test6.FINISHLINE)
        self.game.players[pl].pawns = copy.deepcopy(self.scenes.Test6.PLAYER0PAWNS)
        self.game.players[pl].pawnsHome = self.scenes.Test6.PLAYER0PAWNSHOME
        self.game.players[pl].pawnsFinished = copy.deepcopy(self.scenes.Test6.PLAYER0PAWNSFINISHED)
        self.game.players[pl].strategy = 'furthest'
        self.game.playOneThrow(pl, diceNumber)
        
        if diceNumber == 1:
            return(self.game.board.filledBoard == self.scenes.Test6.BOARDAFTER1 and 
                self.game.board.filledFinishLine == self.scenes.Test6.FINISHLINEAFTER1)
        if diceNumber == 2:
            return(self.game.board.filledBoard == self.scenes.Test6.BOARDAFTER2 and 
                self.game.board.filledFinishLine == self.scenes.Test6.FINISHLINEAFTER2)
        elif diceNumber == 3:
            return(self.game.board.filledBoard == self.scenes.Test6.BOARDAFTER3 and 
                self.game.board.filledFinishLine == self.scenes.Test6.FINISHLINEAFTER3)
        else:
            return(False)
            
    def check_rule7(self):
        pl = 0
        self.game.board.filledBoard = self.scenes.Test7.BOARD
        self.game.board.filledFinishLine = self.scenes.Test7.FINISHLINE
        self.game.players[pl].pawns = self.scenes.Test7.PLAYER0PAWNS
        self.game.players[pl].pawnsHome = self.scenes.Test7.PLAYER0PAWNSHOME
        self.game.players[pl].pawnsFinished = self.scenes.Test7.PLAYER0PAWNSFINISHED
        diceNumber = 2
        self.game.playOneTurn(pl, [diceNumber])
        
        assert self.game.board.filledFinishLine == self.scenes.Test7.FINISHLINEAFTER
        assert self.game.someoneWon == True
        assert self.game.winner == pl
        
    def check_safe_strat(self):
        pl = 2
        self.game.board.filledBoard = self.scenes.TestSafe.BOARD
        self.game.players[pl].pawns = self.scenes.TestSafe.PLAYER2PAWNS
        self.game.players[pl].pawnsHome = self.scenes.TestSafe.PLAYER2PAWNSHOME
        self.game.players[pl].pawnsFinished = self.scenes.TestSafe.PLAYER2PAWNSFINISHED
        self.game.players[pl].strategy = 'safest'
        diceNumber = 3
        self.game.playOneTurn(pl, [diceNumber])
        
        return(self.game.board.filledBoard == self.scenes.TestSafe.BOARDAFTER and
            self.game.board.filledFinishLine == self.scenes.TestSafe.FINISHLINEAFTER)
