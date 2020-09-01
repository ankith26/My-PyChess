In this folder we declare the 'chess.lib' module. This implements all chess features, minimax algorithm for singleplayer and GUI for chess board.


__init__.py - This will be imported when one does from 'chess.lib import *'. Bundles all functions from the lib and also define a few important wrapper functions.
ai.py - This is NOT Artificial Intelligence :). Just implementation of chess player algorithm.
core.py - This is a VERY IMPORTANT module. Defines functions to handle all chess related stuff.
gui.py - As the name suggests, define all gui funcions for chess board.
heuristics.py - Defines a few constants to be used in ai.py
utils.py - Define a few non-gui utility chess functions that are not core-chess related.

For more docmentation of the variables used and such, check docs.txt