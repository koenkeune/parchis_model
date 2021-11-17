from model.visualizer import *
import pygame, sys
from pygame.locals import *

class Scenarios(object):
    EMPTYBOARD = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    
    class Test2_case1():
        BOARD = [[], ['player1pawn2'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player3pawn2'], [], [], ['player1pawn1'], [], [], [], ['player3pawn1'], [], ['player2pawn2'], [], [], [], [], [], [], [], [], [], [], ['player0pawn1'], [], ['player3pawn0', 'player3pawn3'], [], [], [], [], [], [], []]
        BOARDAFTER = [[], ['player1pawn2'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player3pawn2'], [], [], ['player1pawn1'], [], [], [], ['player3pawn1'], [], ['player2pawn2'], [], [], [], [], [], [], [], [], [], [], ['player0pawn1'], [], ['player3pawn0', 'player3pawn3'], [], [], [], [], [], [], []]
        BOARDAFTER2 = [[], ['player1pawn2'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player3pawn2'], [], [], ['player1pawn1'], [], [], [], ['player3pawn1'], [], ['player2pawn2'], [], [], [], [], [], [], [], [], [], [], [], ['player0pawn1'], ['player3pawn0', 'player3pawn3'], [], [], [], [], [], [], []]
        PLAYER0PAWNS = {'player0pawn0': -1, 'player0pawn1': 54, 'player0pawn2': -1, 'player0pawn3': -1}
        PLAYER0PAWNSHOME = 3
        PLAYER0PAWNSFINISHED = 0
        
    class Test2_case2():
        BOARD = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player1pawn1'], [], [], [], [], [], ['player2pawn2'], [], [], [], [], [], [], [], [], [], [], ['player3pawn1'], [], ['player3pawn0'], [], ['player1pawn1', 'player0pawn0'], [], [], [], [], []]
        BOARDAFTER = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player1pawn1'], [], [], [], [], [], ['player2pawn2'], [], [], [], [], [], [], [], [], [], [], ['player3pawn1'], [], [], [], ['player1pawn1', 'player0pawn0'], ['player3pawn0'], [], [], [], []]
        PLAYER3PAWNS = {'player3pawn0': 5, 'player3pawn1': 3, 'player3pawn2': -1, 'player3pawn3': -1}
        PLAYER3PAWNSHOME = 2
        PLAYER3PAWNSFINISHED = 0
    
    class Test2_case3():
        BOARD = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player1pawn1'], [], [], [], [], [], ['player2pawn2'], [], [], [], [], [], [], [], [], [], [], [], ['player3pawn1'], ['player3pawn0', 'player3pawn3'], [], ['player0pawn1', 'player1pawn2'], [], [], [], [], []]
        BOARDAFTER = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player1pawn1'], [], [], [], [], [], ['player2pawn2'], [], [], [], [], [], [], [], [], [], [], [], ['player3pawn1'], ['player3pawn0', 'player3pawn3'], [], ['player0pawn1', 'player1pawn2'], [], [], [], [], []]
        PLAYER3PAWNS = {'player3pawn0': 5, 'player3pawn1': 4, 'player3pawn2': -1, 'player3pawn3': 5}
        PLAYER3PAWNSHOME = 1
        PLAYER3PAWNSFINISHED = 0
    
    class Test3_case1():
        BOARD = [[], [], ['player1pawn2'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player0pawn0'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player3pawn2'], [], [], ['player1pawn1'], [], [], [], ['player3pawn1'], [], ['player2pawn2'], [], ['player0pawn2'], [], [], [], [], [], ['player3pawn0'], [], [], [], ['player0pawn1'], [], [], [], [], ['player3pawn3'], [], [], []]
        BOARDAFTER = [[], ['player2pawn2'], ['player1pawn2'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player0pawn0'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player3pawn2'], [], [], ['player1pawn1'], [], [], [], ['player3pawn1'], [], [], [], [], [], [], [], [], [], ['player3pawn0'], [], [], [], ['player0pawn1'], [], [], [], [], ['player3pawn3'], [], [], []]
        PLAYER2PAWNS = {'player2pawn0': -1, 'player2pawn1': -1, 'player2pawn2': 9, 'player2pawn3': -1}
        PLAYER2PAWNSHOME = 3
        PLAYER2PAWNSFINISHED = 0
        
    class Test3_case2():
        BOARD = [[], ['player1pawn2'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player0pawn0'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player3pawn2'], [], [], ['player1pawn1'], [], [], [], ['player3pawn1'], [], ['player2pawn2'], [], ['player0pawn2'], [], [], [], [], [], ['player3pawn0'], [], [], [], ['player0pawn1'], [], [], [], [], ['player3pawn3'], [], [], []]
        BOARDAFTER = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player0pawn0'], ['player2pawn2'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player3pawn2'], [], [], ['player1pawn1'], [], [], [], ['player3pawn1'], [], [], [], [], [], [], [], [], [], ['player3pawn0'], [], [], [], ['player0pawn1'], [], [], [], [], ['player3pawn3'], [], [], []]
        PLAYER2PAWNS = {'player2pawn0': -1, 'player2pawn1': -1, 'player2pawn2': 9, 'player2pawn3': -1}
        PLAYER2PAWNSHOME = 3
        PLAYER2PAWNSFINISHED = 0
    
    class Test4():
        BOARD = [[], [], ['player1pawn2'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player0pawn0'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player3pawn2'], [], [], ['player1pawn1'], [], [], [], ['player3pawn1'], [], ['player2pawn2'], [], [], ['player0pawn2'], [], [], [], [], ['player3pawn0'], [], [], [], ['player0pawn1'], [], [], [], [], ['player3pawn3'], [], [], []]
        BOARDAFTER = [[], [], ['player1pawn2'], [], ['player0pawn3'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player0pawn0'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player3pawn2'], [], [], ['player1pawn1'], [], [], [], ['player3pawn1'], [], ['player2pawn2'], [], [], ['player0pawn2'], [], [], [], [], ['player3pawn0'], [], [], [], ['player0pawn1'], [], [], [], [], ['player3pawn3'], [], [], []]
        PLAYER0PAWNS = {'player0pawn0': 16, 'player0pawn1': 55, 'player0pawn2': 46, 'player0pawn3': -1}
        PLAYER0PAWNSHOME = 1
        PLAYER0PAWNSFINISHED = 0
    
    class Test4_1a():    
        BOARD = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player0pawn0'], ['player1pawn0', 'player1pawn2'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player3pawn2'], [], [], ['player1pawn1'], [], [], [], ['player3pawn1'], [], ['player2pawn2'], [], [], ['player0pawn2'], [], [], [], [], ['player3pawn0'], [], [], [], ['player0pawn1'], [], [], [], [], ['player3pawn3'], [], [], []]
        BOARDAFTER = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player0pawn0'], ['player1pawn0', 'player1pawn2'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player3pawn2'], [], [], [], [], [], [], ['player3pawn1'], ['player1pawn1'], ['player2pawn2'], [], [], ['player0pawn2'], [], [], [], [], ['player3pawn0'], [], [], [], ['player0pawn1'], [], [], [], [], ['player3pawn3'], [], [], []]
        PLAYER1PAWNS = {'player1pawn0': 0, 'player1pawn1': 20, 'player1pawn2': 0, 'player1pawn3': -1}
        PLAYER1PAWNSHOME = 1
        PLAYER1PAWNSFINISHED = 0
    
    class Test4_1b():
        BOARD = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player0pawn0'], ['player1pawn0', 'player1pawn2'], [], [], [], [], ['player1pawn3'], [], [], [], [], [], [], [], [], [], [], [], ['player3pawn2'], [], [], ['player1pawn1'], [], [], [], ['player3pawn1'], [], ['player2pawn2'], [], [], ['player0pawn2'], [], [], [], [], ['player3pawn0'], [], [], [], ['player0pawn1'], [], [], [], [], ['player3pawn3'], [], [], []]
        BOARDAFTER = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player0pawn0'], ['player1pawn0', 'player1pawn2'], [], [], [], [], ['player1pawn3'], [], [], [], [], [], [], [], [], [], [], [], ['player3pawn2'], [], [], [], [], [], [], ['player3pawn1'], ['player1pawn1'], ['player2pawn2'], [], [], ['player0pawn2'], [], [], [], [], ['player3pawn0'], [], [], [], ['player0pawn1'], [], [], [], [], ['player3pawn3'], [], [], []]
        PLAYER1PAWNS = {'player1pawn0': 0, 'player1pawn1': 20, 'player1pawn2': 0, 'player1pawn3': 5}
        PLAYER1PAWNSHOME = 0
        PLAYER1PAWNSFINISHED = 0
        
    class Test4_2():
        BOARD = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player0pawn0'], ['player1pawn0', 'player1pawn2'], [], [], [], [], ['player1pawn3'], [], [], [], [], [], [], [], [], [], [], [], ['player3pawn2', 'player1pawn1'], [], [], [], [], [], [], ['player3pawn1'], [], ['player2pawn2'], [], [], ['player0pawn2'], [], [], [], [], ['player3pawn0'], [], [], [], ['player0pawn1'], [], [], [], [], ['player3pawn3'], [], [], []]
        BOARDAFTER = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player0pawn0'], ['player1pawn0', 'player1pawn2'], [], [], [], [], ['player1pawn3'], [], [], [], [], [], [], [], [], [], [], [], ['player3pawn2', 'player2pawn0'], [], [], [], [], [], [], ['player3pawn1'], [], [], [], [], ['player0pawn2'], [], [], [], [], ['player3pawn0'], [], [], [], ['player0pawn1'], [], [], [], [], ['player3pawn3'], [], [], ['player2pawn2']]
        PLAYER2PAWNS = {'player2pawn0': -1, 'player2pawn1': -1, 'player2pawn2': 9, 'player2pawn3': -1}
        PLAYER2PAWNSHOME = 3
        PLAYER2PAWNSFINISHED = 0
        
    class Test5():
        BOARD = [[], [], ['player1pawn2'], [], ['player0pawn0'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player3pawn2'], [], [], ['player1pawn1'], [], [], [], ['player3pawn1'], [], ['player2pawn2'], [], [], [], [], [], [], [], ['player3pawn0'], [], [], [], [], [], [], [], [], ['player3pawn3'], [], [], []]
        BOARDAFTER = [[], [], ['player1pawn2'], [], [], [], [], [], [], [], [], [], [], ['player0pawn0'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player3pawn2'], [], [], ['player1pawn1'], [], [], [], ['player3pawn1'], [], ['player2pawn2'], [], [], [], [], [], [], [], ['player3pawn0'], [], [], [], [], [], [], [], [], ['player3pawn3'], [], [], []]
        PLAYER0PAWNS = {'player0pawn0': 0, 'player0pawn1': -1, 'player0pawn2': -1, 'player0pawn3': -1}
        PLAYER0PAWNSHOME = 3
        PLAYER0PAWNSFINISHED = 0
        
    class Test5_1():
        BOARD = [[], [], ['player1pawn2'], [], ['player0pawn0'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player3pawn2'], [], [], ['player1pawn1'], [], [], [], ['player3pawn1'], [], ['player2pawn2'], [], [], [], [], [], [], [], ['player3pawn0'], [], [], [], [], [], [], [], [], ['player3pawn3'], [], [], []]
        BOARDAFTER = [[], [], ['player1pawn2'], [], [], [], [], [], [], [], [], ['player0pawn0'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player3pawn2'], [], [], ['player1pawn1'], [], [], [], ['player3pawn1'], [], ['player2pawn2'], [], [], [], [], [], [], [], ['player3pawn0'], [], [], [], [], [], [], [], [], ['player3pawn3'], [], [], []]
        PLAYER0PAWNS = {'player0pawn0': 0}
        PLAYER0PAWNSHOME = 0
        PLAYER0PAWNSFINISHED = 3    
    
    class Test5_2_case1():
        BOARD = [[], [], ['player1pawn2'], [], ['player0pawn0', 'player0pawn1'], [], [], [], [], [], [], ['player0pawn2'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player3pawn2'], [], [], ['player1pawn1'], [], [], [], ['player3pawn1'], [], ['player2pawn2'], [], [], [], [], [], [], [], ['player3pawn0'], [], [], [], [], [], [], [], [], ['player3pawn3'], [], [], []]
        BOARDAFTER = [[], [], ['player1pawn2'], [], ['player0pawn0'], [], [], [], [], [], ['player0pawn1'], [], ['player0pawn2'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player3pawn2'], [], [], ['player1pawn1'], [], [], [], ['player3pawn1'], [], ['player2pawn2'], [], [], [], [], [], [], [], ['player3pawn0'], [], [], [], [], [], [], [], [], ['player3pawn3'], [], [], []]
        PLAYER0PAWNS = {'player0pawn0': 0, 'player0pawn1': 0, 'player0pawn2': 7, 'player0pawn3': -1}
        PLAYER0PAWNSHOME = 1
        PLAYER0PAWNSFINISHED = 0
        
    class Test5_2_case2():
        BOARD = [[], [], [], [], ['player0pawn0', 'player1pawn2'], [], [], [], [], [], [], ['player0pawn2'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player3pawn2'], [], [], ['player1pawn1'], [], [], [], ['player3pawn1'], [], ['player2pawn2'], [], [], [], [], [], [], [], ['player3pawn0'], [], [], [], [], [], [], [], [], ['player3pawn3'], [], [], []]
        BOARDAFTER = [[], [], [], [], ['player0pawn0', 'player1pawn2'], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player0pawn2'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player3pawn2'], [], [], ['player1pawn1'], [], [], [], ['player3pawn1'], [], ['player2pawn2'], [], [], [], [], [], [], [], ['player3pawn0'], [], [], [], [], [], [], [], [], ['player3pawn3'], [], [], []]
        PLAYER0PAWNS = {'player0pawn0': 0, 'player0pawn1': -1, 'player0pawn2': 7, 'player0pawn3': -1}
        PLAYER0PAWNSHOME = 2
        PLAYER0PAWNSFINISHED = 0    
    
    class Test5_3():
        BOARD = [[], [], ['player1pawn2'], [], ['player0pawn0'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player3pawn2'], [], [], ['player1pawn1'], [], [], [], ['player3pawn1'], [], ['player2pawn2'], [], [], [], [], [], [], [], ['player3pawn0'], [], [], [], [], [], [], [], [], ['player3pawn3'], [], [], []]
        BOARDAFTER = [[], [], ['player1pawn2'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player3pawn2'], [], [], ['player1pawn1'], [], [], [], ['player3pawn1'], [], ['player2pawn2'], [], [], [], [], [], [], [], ['player3pawn0'], [], [], [], [], [], [], [], [], ['player3pawn3'], [], [], []]
        PLAYER0PAWNS = {'player0pawn0': 0, 'player0pawn1': -1, 'player0pawn2': -1, 'player0pawn3': -1}
        PLAYER0PAWNSHOME = 3
        PLAYER0PAWNSFINISHED = 0
    
    class Test5_3a_case1():
        BOARD = [[], [], ['player1pawn2'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player3pawn2'], [], [], ['player1pawn1'], [], [], [], ['player3pawn1'], [], ['player2pawn2'], [], ['player0pawn0'], [], [], [], [], [], ['player3pawn0'], [], [], [], [], [], [], [], [], ['player3pawn3'], [], [], []]
        BOARDAFTER = [[], [], ['player1pawn2'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player3pawn2'], [], [], ['player1pawn1'], [], [], [], ['player3pawn1'], [], ['player2pawn2'], [], [], [], [], [], [], [], ['player3pawn0'], [], [], [], [], [], [], [], [], ['player3pawn3'], [], [], []]           
        FINISHLINE = [[[], [], [], [], [], [], []], [[], [], [], [], [], [], []], [[], [], [], [], [], [], []], [[], [], [], [], [], [], []]]
        FINISHLINEAFTER = [[[], [], [], [], [], [], []], [[], [], [], [], [], [], []], [[], [], [], [], [], [], []], [[], [], [], [], [], [], []]]
        PLAYER0PAWNS = {'player0pawn0': 45, 'player0pawn1': -1, 'player0pawn2': -1, 'player0pawn3': -1}
        PLAYER0PAWNSHOME = 3
        PLAYER0PAWNSFINISHED = 0
        
    class Test5_3a_case2():
        BOARD = [[], [], ['player1pawn2'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player3pawn2'], [], [], ['player1pawn1'], [], [], [], ['player3pawn1'], [], ['player2pawn2'], [], [], ['player0pawn0'], [], [], [], [], ['player3pawn0'], [], [], [], [], [], [], [], [], ['player3pawn3'], [], [], []]
        BOARDAFTER = [[], [], ['player1pawn2'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player3pawn2'], [], [], ['player1pawn1'], [], [], [], ['player3pawn1'], [], ['player2pawn2'], [], [], [], [], [], [], [], ['player3pawn0'], [], [], [], [], [], [], [], [], ['player3pawn3'], [], [], []]
        FINISHLINE = [[[], [], [], [], [], [], []], [[], [], [], [], [], [], []], [[], [], [], [], [], [], []], [[], [], [], [], [], [], []]]
        FINISHLINEAFTER = [[['player0pawn0'], [], [], [], [], [], []], [[], [], [], [], [], [], []], [[], [], [], [], [], [], []], [[], [], [], [], [], [], []]]
        PLAYER0PAWNS = {'player0pawn0': 46, 'player0pawn1': -1, 'player0pawn2': -1, 'player0pawn3': -1}
        PLAYER0PAWNSHOME = 3
        PLAYER0PAWNSFINISHED = 0
        
    class Test6():
        BOARD = [[], [], ['player1pawn2'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player3pawn2'], [], [], ['player1pawn1'], [], [], [], ['player3pawn1'], [], ['player2pawn2'], [], [], ['player0pawn0'], [], [], [], [], ['player3pawn0'], [], [], [], [], [], [], [], [], ['player3pawn3'], [], [], []]
        BOARDAFTER1 = [[], [], ['player1pawn2'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player3pawn2'], [], [], ['player1pawn1'], [], [], [], ['player3pawn1'], [], ['player2pawn2'], [], [], ['player0pawn0'], [], [], [], [], ['player3pawn0'], [], [], [], [], [], [], [], [], ['player3pawn3'], [], [], []]
        BOARDAFTER2 = [[], [], ['player1pawn2'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player3pawn2'], [], [], ['player1pawn1'], [], [], [], ['player3pawn1'], [], ['player2pawn2'], [], [], [], [], [], [], [], ['player3pawn0'], [], [], [], [], ['player0pawn0'], [], [], [], ['player3pawn3'], [], [], []]
        BOARDAFTER3 = [[], [], ['player1pawn2'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player3pawn2'], [], [], ['player1pawn1'], [], [], [], ['player3pawn1'], [], ['player2pawn2'], [], [], [], [], [], ['player0pawn0'], [], ['player3pawn0'], [], [], [], [], [], [], [], [], ['player3pawn3'], [], [], []]
        FINISHLINE = [[[], [], [], [], [], ['player0pawn1'], []], [[], [], [], [], [], [], []], [[], [], [], [], [], [], []], [[], [], [], [], [], [], []]]
        FINISHLINEAFTER1 = [[[], [], [], [], [], [], ['player0pawn1']], [[], [], [], [], [], [], []], [[], [], [], [], [], [], []], [[], [], [], [], [], [], []]]
        FINISHLINEAFTER2 = [[[], [], [], [], [], [], []], [[], [], [], [], [], [], []], [[], [], [], [], [], [], []], [[], [], [], [], [], [], []]]
        FINISHLINEAFTER3 = [[[], [], [], [], [], ['player0pawn1'], []], [[], [], [], [], [], [], []], [[], [], [], [], [], [], []], [[], [], [], [], [], [], []]]
        PLAYER0PAWNS = {'player0pawn0': 46, 'player0pawn1': 69, 'player0pawn2': -1, 'player0pawn3': -1}
        PLAYER0PAWNSHOME = 2
        PLAYER0PAWNSFINISHED = 0
        
    class Test7():
        BOARD = [[], [], [], [], [], [], [], [], [], [], [], ['player2pawn3'], [], [], [], [], [], [], [], [], [], ['player1pawn2'], [], [], [], [], [], [], [], [], [], ['player2pawn2'], [], ['player1pawn1'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
        FINISHLINE = [[[], [], [], [], [], ['player0pawn3'], []], [[], [], [], [], [], [], ['player1pawn0']], [[], [], [], [], [], [], []], [[], [], [], [], [], [], []]]
        FINISHLINEAFTER = [[[], [], [], [], [], [], []], [[], [], [], [], [], [], ['player1pawn0']], [[], [], [], [], [], [], []], [[], [], [], [], [], [], []]]
        PLAYER0PAWNS = {'player0pawn3': 69}
        PLAYER0PAWNSHOME = 0
        PLAYER0PAWNSFINISHED = 3
            
def visualizeScenario(scenario, filledFinishLine = []):
    w = 800
    h = 800
    pygame.init()
    screen = pygame.display.set_mode((w, h))
    drawBoard(screen, w, h)
    drawPawnsOnBoard(screen, scenario)
    if filledFinishLine:
        drawPawnsAtFinishline(screen, filledFinishLine)
    while(True):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()