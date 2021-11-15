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
        assert tester.check_rule1()
    
    def test_rule2(self):
        tester = RulesTester(self.game)
        assert tester.check_rule2(2)
        assert tester.check_rule2(3)
        
    def test_rule2_1(self):
        tester = RulesTester(self.game)
        assert tester.check_rule2_1()
        
    def test_rule3(self):
        tester = RulesTester(self.game)
        assert tester.check_rule3_case1()
        assert tester.check_rule3_case2()
        
    def test_rule4(self):
        tester = RulesTester(self.game)
        assert tester.check_rule4()
        
    def test_rule4_1a(self):
        tester = RulesTester(self.game)
        assert tester.check_rule4_1a() 

    def test_rule4_1b(self):
        tester = RulesTester(self.game)
        assert tester.check_rule4_1b()
        
    def test_rule4_2(self):
        tester = RulesTester(self.game)
        assert tester.check_rule4_2()
        
        
if __name__ == "__main__":
    unittest.main()
