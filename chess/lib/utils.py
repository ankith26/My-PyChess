"""
This file is a file of My-PyChess application.
In this file, we define a few other non-gui MyPyChess helper functions.

Level of development = STABLE
"""

from datetime import datetime
import os

LETTER = ["", "a", "b", "c", "d", "e", "f", "g", "h"]

# encode() essentially converts a form of data used by the game to denote moves
# into the standard full algebraic notation (the kind that is used to
# communicate with a chess engine).
# To know more about the data format used by this game, checkout multiplayer.py
def encode(fro, to, promote=None):
    data = LETTER[fro[0]] + str(9 - fro[1]) + LETTER[to[0]] + str(9 - to[1])
    if promote is not None:
        return data + promote
    return data

# decode does the opposite of encode()
def decode(data):
    if len(data) == 4:
        return (
            [LETTER.index(data[0]), 9 - int(data[1])],
            [LETTER.index(data[2]), 9 - int(data[3])],
            None,
        )
    elif len(data) == 5:
        return (
            [LETTER.index(data[0]), 9 - int(data[1])],
            [LETTER.index(data[2]), 9 - int(data[3])],
            data[4],
        )
    
# A simple function to undo, num corresponds to the number of moves to undo.
def undo(moves, num=1):
    temp = moves.strip().split(" ")
    if len(temp) in range(num):
        return moves.strip()
    else:
        return " ".join(temp[:-num])
    
# Get path to stockfish executable from path.txt config file
def getSFpath():
    conffile = os.path.join("res", "stockfish", "path.txt")
    if os.path.exists(conffile):
        with open(conffile, "r") as f:
            return f.read().strip()

# Remove stockfish config path file.
def rmSFpath():
    os.remove(os.path.join("res", "stockfish", "path.txt")) 

# This function saves a game into a text file.
# It does this by saving all moves in long algebraic notation
def saveGame(moves, gametype="multi", player=0, level=0, cnt=0):
    if cnt >= 20:
        return -1

    name = os.path.join("res", "savedGames", "game" + str(cnt) + ".txt")
    if os.path.isfile(name):
        return saveGame(moves, gametype, player, level, cnt + 1)
    
    else:
        if gametype == "single":
            gametype += " " + str(player) + " " + str(level)
        if gametype == "mysingle":
            gametype += " " + str(player)

        dt = datetime.now()
        date = "/".join(map(str, [dt.day, dt.month, dt.year]))
        time = ":".join(map(str, [dt.hour, dt.minute, dt.second]))

        text = "\n".join([gametype, " ".join([date, time]), moves.strip()])
        with open(name, "w") as file:
            file.write(text + "\n")
        return cnt
