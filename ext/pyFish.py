"""
This file is a part of My-PyChess application.

Here I have written a python interface class for stockfish chess engine.
This is used in the singleplayer mode of My-PyChess.
"""

import queue
import subprocess
import threading

_LEVELDATA = (
    (0, 10, 1),
    (1, 50, 1),
    (3, 80, 2),
    (6, 160, 4),
    (8, 250, 6),
    (10, 400, 8),
    (12, 500, 10),
    (14, 700, 12),
    (16, 900, 16),
)

# StockFish class to interface with stockfish chess engine.
class StockFish:
    def __init__(self, path="stockfish", level=1):
        self.moves = []
        self.skill, self.movetime, self.depth = _LEVELDATA[level - 1]

        self.thread = threading.Thread()
        self.q = queue.Queue(1)

        try:
            self.stockfish = subprocess.Popen(
                path,
                universal_newlines=True,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
            )

            if self.stockfish.stdout.readline().split()[0].lower() == "stockfish":
                self.active = True
                self._put("uci")
                self.setOption("Skill Level", self.skill)
            else:
                self.active = False
                self.stockfish.terminate()

        except:
            self.active = False

    def _raiseErrorIfInactive(self):
        if not self.active:
            raise RuntimeError("Intergration with stockfish engine has failed")

    def _put(self, command):
        self._raiseErrorIfInactive()
        self.stockfish.stdin.write(str(command) + "\n")
        self.stockfish.stdin.flush()

    def _isReady(self):
        self._raiseErrorIfInactive()
        self._put("isready")
        while True:
            if self.stockfish.stdout.readline().strip() == "readyok":
                return

    def _engine(self):
        self._isReady()
        self._put("position startpos moves " + " ".join(self.moves))
        self._put("go depth {} movetime {}".format(self.depth, self.movetime))
        while True:
            msg = self.stockfish.stdout.readline().strip().split(" ")
            if msg[0] == "bestmove":
                if msg[1] == "(none)":
                    self.q.put(None)
                else:
                    self.q.put(msg[1])
                break

    def isActive(self):
        return self.active

    def startGame(self, moves=""):
        self._isReady()
        self._put("ucinewgame")
        self.moves = moves.split()

    def setOption(self, name, value):
        self._isReady()
        self._put("setoption name {} value {}".format(name, value))

    def startEngine(self):
        self._raiseErrorIfInactive()
        if not self.thread.is_alive() and self.q.empty():
            self.thread = threading.Thread(target=self._engine)
            self.thread.start()
        else:
            raise RuntimeError("Could not start engine")

    def makeMove(self, move):
        self.moves.append(move)
        self.startEngine()

    def getMove(self, block=True):
        self._raiseErrorIfInactive()
        if not self.hasMoved() and not block:
            self._put("stop")
        
        enginemove = self.q.get()
        self.moves.append(enginemove)
        return enginemove

    def hasMoved(self):
        self._raiseErrorIfInactive()
        return not self.q.empty() and not self.thread.is_alive()

    def undo(self, num=1):
        self._raiseErrorIfInactive()
        if not self.thread.is_alive():
            if len(self.moves) not in range(num):
                self.moves = self.moves[:-num]

    def close(self):
        self._isReady()
        self._put("quit")
        self.stockfish.terminate()
        self.active = False

# A simple function to test wether a stockfish executable works or not.
# Path to stockfish must be specified as an argument
def teststockfish(path):
    fish = StockFish(path)
    stat = fish.isActive()
    if stat:
        fish.close()
    return stat