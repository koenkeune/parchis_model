# Parchis Model
 Runs multiple games of parchis to find out what strategy is better safe or agressive? There is also the option to play it yourself.
 
 
 How To Use
---------------
Install pygame: `python -m pip install "pygame"`
and unittest: `python -m pip install "unittest"`

Run the code: `python model/play.py [runs]` 

Test the code: `python testing/mainTester.py -v`

'runs' is an optional parameter to specify the number of runs it should do. Without it you will have to play the game yourself against the computer. You make the game go forward with the enter key or the spacebar and you make a move with 1/2/3/4. The board along with the dice number thrown and the pawns to move will be printed.

'mainTester' tests if the rules specified in sources/rules.txt are correctly implemented. It confirms the tests by showing 'ok', else it would show 'FAIL' or 'ERROR'.
