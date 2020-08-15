"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    total = 0
    for row in board:
        for element in row:
            if element is not None:
                total += 1

    if total % 2 == 0:
        return("X")
    return ("O")


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for row_index, row in enumerate(board):
        for column_index, element in enumerate(row):
            if element is None:
                moves.add((row_index, column_index))

    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if terminal(board):
        raise ValueError("Game over.")
    elif action not in actions(board):
        raise ValueError("Invalid action.")
    else:
        p = player(board)
        result_board = copy.deepcopy(board)
        (i, j) = action
        result_board[i][j] = p

    return result_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # check horizontally
    if horizontal_check(board, X):
        return X
    if horizontal_check(board, O):
        return O
    # check vertically
    if vertical_check(board, X):
        return X
    if vertical_check(board, O):
        return O
    # check diagonally for X
    if diagonal_check(board, X):
        return X
    # check diagonally for O
    if diagonal_check(board, O):
        return O
    # check antidiagonally for X
    if anti_diagonal_check(board, X):
        return X
    # check antidiagonally for O
    if anti_diagonal_check(board, O):
        return O
    return None


def horizontal_check(board, player):
    for i in range(3):
        total = 0
        for j in range(3):
            if board[i][j] == player:
                total += 1
        if total == 3:
            return True
    return False


def vertical_check(board, player):
    for j in range(3):
        total = 0
        for i in range(3):
            if board[i][j] == player:
                total += 1
        if total == 3:
            return True


def diagonal_check(board, player):
    if board[0][0] == (player) and board[1][1] == (player) and board[2][2] == (player):
        return True
    return False


def anti_diagonal_check(board, player):
    if board[0][2] == (player) and board[1][1] == (player) and board[2][0] == (player):
        return True
    return False


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    for row in board:
        for element in row:
            if element is None:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    p = player(board)

    # If empty board is provided as input, return corner.
    if board == [[EMPTY]*3]*3:
        return (0, 0)

    if p == X:
        v = float("-inf")
        selected_action = None
        for action in actions(board):
            minValueResult = minValue(result(board, action))
            if minValueResult > v:
                v = minValueResult
                selected_action = action
    elif p == O:
        v = float("inf")
        selected_action = None
        for action in actions(board):
            maxValueResult = maxValue(result(board, action))
            if maxValueResult < v:
                v = maxValueResult
                selected_action = action

    return selected_action


def maxValue(board):
    if terminal(board):
        return utility(board)
    v = float("-inf")
    for action in actions(board):
        v = max(v, minValue(result(board, action)))

    return v


def minValue(board):
    if terminal(board):
        return utility(board)
    v = float("inf")
    for action in actions(board):
        v = min(v, maxValue(result(board, action)))

    return v
