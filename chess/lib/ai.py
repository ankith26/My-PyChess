"""
This file is a file of My-PyChess application.
In this file, we implement a basic chess player algorithm in python.

This implementation is a weak player of chess.
This algorithm is not fast or efficient as any C impemenation of the same,
just an attempt to display the workings of the minimax algorithm with
alpha-beta pruning in Python.
"""

from chess.lib.core import copy, legalMoves, updateFlags, move
from chess.lib.heuristics import *

INF = 1000000
DEPTH = 2

# This is a wrapper function for the 'move' function in the chess lib.
# It makes the move AND updates the flags and returns both
def makeMove(side, board, fro, to, flags):
    newboard = move(side, copy(board), fro, to)
    newflags = updateFlags(side, newboard, fro, to, list(flags[0]))
    return newboard, newflags

# This is a rudementary and simple evaluative function for a given state of
# board. It gives each piece a value based on its position on the board,
# returns a numeric representation of the board
def evaluate(board):
    var = 0
    for x, y, piece in board[0]:
        if piece == "p":
            var += 1 + pawnEvalWhite[y - 1][x - 1]
        elif piece == "b":
            var += 9 + bishopEvalWhite[y - 1][x - 1]
        elif piece == "n":
            var += 9 + knightEval[y - 1][x - 1]
        elif piece == "r":
            var += 14 + rookEvalWhite[y - 1][x - 1]
        elif piece == "q":
            var += 25 + queenEval[y - 1][x - 1]
        elif piece == "k":
            var += 200 + kingEvalWhite[y - 1][x - 1]

    for x, y, piece in board[1]:
        if piece == "p":
            var -= 1 + pawnEvalBlack[y - 1][x - 1]
        elif piece == "b":
            var -= 9 + bishopEvalBlack[y - 1][x - 1]
        elif piece == "n":
            var -= 9 + knightEval[y - 1][x - 1]
        elif piece == "r":
            var -= 14 + rookEvalBlack[y - 1][x - 1]
        elif piece == "q":
            var -= 25 + queenEval[y - 1][x - 1]
        elif piece == "k":
            var -= 200 + kingEvalBlack[y - 1][x - 1]

    return var

# This is the MiniMax function, implemented with alpha-beta pruning.
def miniMax(side, board, flags, depth=DEPTH, alpha=-INF, beta=INF):
    if depth == 0:
        return evaluate(board)

    if not side:
        bestVal = -INF
        for fro, to in legalMoves(side, board, flags):
            movedata = makeMove(side, board, fro, to, flags)
            nodeVal = miniMax(1, *movedata, depth - 1, alpha, beta)
            if nodeVal > bestVal:
                bestVal = nodeVal
                if depth == DEPTH:
                    bestMove = (fro, to)
            alpha = max(alpha, bestVal)
            if alpha >= beta:
                break

    else:
        bestVal = INF
        for fro, to in legalMoves(side, board, flags):
            movedata = makeMove(side, board, fro, to, flags)
            nodeVal = miniMax(0, *movedata, depth - 1, alpha, beta)
            if nodeVal < bestVal:
                bestVal = nodeVal
                if depth == DEPTH:
                    bestMove = (fro, to)
            beta = min(beta, bestVal)
            if alpha >= beta:
                break

    if depth == DEPTH:
        return bestMove
    else:
        return bestVal
