"""Unbeatable Tic-Tac-Toe engine: minimax + alpha-beta pruning.

Board = list of 9 cells, each "X", "O" or " ".  Index layout:
 0 | 1 | 2
 3 | 4 | 5
 6 | 7 | 8
"""
import random

LINES = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
# Greedy move ordering (centre, corners, edges) makes pruning cut far more branches.
ORDER = [4, 0, 2, 6, 8, 1, 3, 5, 7]


def winner(board):
    """Return (symbol, line) of the winner, or (None, None)."""
    for a, b, c in LINES:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a], (a, b, c)
    return None, None


def is_full(board):
    return " " not in board


def _alphabeta(board, player, ai, depth, alpha, beta):
    w, _ = winner(board)
    if w:
        # Prefer quicker wins, slower losses.
        return 10 - depth if w == ai else depth - 10
    if is_full(board):
        return 0
    other = "O" if player == "X" else "X"
    if player == ai:  # maximising
        best = -100
        for m in ORDER:
            if board[m] == " ":
                board[m] = player
                best = max(best, _alphabeta(board, other, ai, depth + 1, alpha, beta))
                board[m] = " "
                alpha = max(alpha, best)
                if alpha >= beta:
                    break
        return best
    best = 100  # minimising
    for m in ORDER:
        if board[m] == " ":
            board[m] = player
            best = min(best, _alphabeta(board, other, ai, depth + 1, alpha, beta))
            board[m] = " "
            beta = min(beta, best)
            if alpha >= beta:
                break
    return best


def best_move(board, ai):
    """Return the optimal cell index for `ai` ("X" or "O"). Never loses."""
    board = list(board)
    if all(c == " " for c in board):
        return random.choice([0, 2, 4, 6, 8])  # all optimal openings
    other = "O" if ai == "X" else "X"
    best_score, best_idx = -100, None
    for m in ORDER:
        if board[m] == " ":
            board[m] = ai
            score = _alphabeta(board, other, ai, 1, -100, 100)
            board[m] = " "
            if score > best_score:
                best_score, best_idx = score, m
    return best_idx
