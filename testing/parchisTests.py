from model.game import *
from random import shuffle

class RulesTester():
    def __init__(self, game):
        self.game = game
        
    def check_rule1_simGame(self):
        strategies = []
        for player in self.game.players:
            strategies.append(player.strategy)
        numPlayers = len(set(strategies))
        starts = []
        for i in range(100):
            shuffle(strategies)
            starts.append(strategies[0])
            
        return(len(set(starts)) == numPlayers)

    def check_rule1_playGame(self):
        numPlayers = len(self.game.players)
        starts = []
        for i in range(100):
            starts.append(throwDiceForStart(numPlayers, False))
            
        return(len(set(starts)) == numPlayers)
        
        
        
        
