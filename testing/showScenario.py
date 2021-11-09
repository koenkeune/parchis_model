import os, sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__)) # make sure it can access model folder
sys.path.append(os.path.dirname(SCRIPT_DIR))
from scenarios import *

scenes = Scenarios()
visualizeScenario(scenes.TEST2BOARD)
