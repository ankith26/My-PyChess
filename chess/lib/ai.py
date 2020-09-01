"""
This file is a part of My-PyChess application.
In this file, we implement a basic chess player algorithm in python.

This implementation is a weak player of chess.
This algorithm is not fast or efficient as any C impemenation of the same,
just an attempt to display the workings of the minimax algorithm with
alpha-beta pruning in Python.
"""

from chess.lib.core import legalMoves, makeMove
from chess.lib.heuristics import *

INF = 1000000
DEPTH = 2

# This is a rudementary and simple evaluative function for a given state of
# board. It gives each piece a value based on its position on the board,
# returns a numeric representation of the board
def evaluate(board):
    score = 0
    for x, y, piece in board[0]:
        if piece == "p":
            score += 1 + pawnEvalWhite[y - 1][x - 1]
        elif piece == "b":
            score += 9 + bishopEvalWhite[y - 1][x - 1]
        elif piece == "n":
            score += 9 + knightEval[y - 1][x - 1]
        elif piece == "r":
            score += 14 + rookEvalWhite[y - 1][x - 1]
        elif piece == "q":
            score += 25 + queenEval[y - 1][x - 1]
        elif piece == "k":
            score += 200 + kingEvalWhite[y - 1][x - 1]

    for x, y, piece in board[1]:
        if piece == "p":
            score -= 1 + pawnEvalBlack[y - 1][x - 1]
        elif piece == "b":
            score -= 9 + bishopEvalBlack[y - 1][x - 1]
        elif piece == "n":
            score -= 9 + knightEval[y - 1][x - 1]
        elif piece == "r":
            score -= 14 + rookEvalBlack[y - 1][x - 1]
        elif piece == "q":
            score -= 25 + queenEval[y - 1][x - 1]
        elif piece == "k":
            score -= 200 + kingEvalBlack[y - 1][x - 1]

    return score

# This is the Mini-Max algorithm, implemented with alpha-beta pruning.
def miniMax(side, board, flags, depth=DEPTH, alpha=-INF, beta=INF):
    if depth == 0:
        return evaluate(board)

    if not side:
        bestVal = -INF
        for fro, to in legalMoves(side, board, flags):
            movedata = makeMove(side, board, fro, to, flags)
            nodeVal = miniMax(*movedata, depth - 1, alpha, beta)
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
            nodeVal = miniMax(*movedata, depth - 1, alpha, beta)
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
