from model.visualizer import *
import pygame, sys
from pygame.locals import *

class Scenarios(object):
    EMPTYBOARD = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    
    class Test2():
        BOARD = [[], ['player1pawn2'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player3pawn2'], [], [], ['player1pawn1'], [], [], [], ['player3pawn1'], [], ['player2pawn2'], [], [], [], [], [], [], [], [], [], [], ['player0pawn1'], [], ['player3pawn0', 'player3pawn3'], [], [], [], [], [], [], []]
        BOARDAFTER = [[], ['player1pawn2'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player3pawn2'], [], [], ['player1pawn1'], [], [], [], ['player3pawn1'], [], ['player2pawn2'], [], [], [], [], [], [], [], [], [], [], ['player0pawn1'], [], ['player3pawn0', 'player3pawn3'], [], [], [], [], [], [], []]
        BOARDAFTER2 = [[], ['player1pawn2'], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player3pawn2'], [], [], ['player1pawn1'], [], [], [], ['player3pawn1'], [], ['player2pawn2'], [], [], [], [], [], [], [], [], [], [], [], ['player0pawn1'], ['player3pawn0', 'player3pawn3'], [], [], [], [], [], [], []]
        PLAYER0PAWNS = {'player0pawn0': -1, 'player0pawn1': 54, 'player0pawn2': -1, 'player0pawn3': -1}
        PLAYER0PAWNSHOME = 3
        PLAYER0PAWNSFINISHED = 0
        
    class Test2_1():
        BOARD = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player1pawn1'], [], [], [], [], [], ['player2pawn2'], [], [], [], [], [], [], [], [], [], [], ['player3pawn1'], [], ['player3pawn0', 'player3pawn3'], [], ['player0pawn1', 'player1pawn2'], [], [], [], [], []]
        BOARDAFTER = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], ['player1pawn1'], [], [], [], [], [], ['player2pawn2'], [], [], [], [], [], [], [], [], [], [], ['player3pawn1'], [], ['player3pawn0', 'player3pawn3'], [], ['player0pawn1', 'player1pawn2'], [], [], [], [], []]
        PLAYER0PAWNS = {'player3pawn0': 5, 'player3pawn1': 3, 'player3pawn2': -1, 'player3pawn3': 5}
        PLAYER0PAWNSHOME = 1
        PLAYER0PAWNSFINISHED = 0
    
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
        
    
            
def visualizeScenario(scenario):
    w = 800
    h = 800
    pygame.init()
    screen = pygame.display.set_mode((w, h))
    drawBoard(screen, w, h)
    drawPawnsOnBoard(screen, scenario)
    while(True):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()