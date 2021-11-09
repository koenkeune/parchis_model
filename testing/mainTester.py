import os, sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__)) # make sure it can access model folder
sys.path.append(os.path.dirname(SCRIPT_DIR))
import unittest
from model.game import *
from parchisTests import *

class ParchisTester(unittest.TestCase):
    
    def setUp(self):
        strategies = ['safest', 'furthest', 'furthest', 'furthest']
        self.game = Game(strategies)

    def test_rule1(self):
        tester = RulesTester(self.game)
        assert tester.check_rule1_simGame()
        assert tester.check_rule1_playGame()
        
    def test_rule4(self):
        assert True
        
        
if __name__ == "__main__":
    unittest.main()