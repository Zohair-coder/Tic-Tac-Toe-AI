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
    if len(action) != 2 or action[0] > 2 or action[0] < 0 or action[1] > 2 or action[1] < 0:
        raise Exception("Invalid action")

    new_board = copy.deepcopy(board)

    turn = player(board)
    new_board[action[0]][action[1]] = turn
    return new_board


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
    if winner(board) == None:
        return False

    for row in board:
        for element in row:
            if element == None:
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

    if p == X:
        best_action = None
        v = -2

        for action in actions(board):
            min_result = min_value(result(board, action))
            if min_result > v:
                v = min_result
                best_action = action
    elif p == O:
        v = 2
        best_action = None
        for action in actions(board):
            max_result = max_value(result(board, action))
            if max_result < v:
                v = max_result
                best_action = action
    return best_action


def min_value(board):
    if terminal(board):
        return utility(board)
    v = -2

    for action in actions(board):
        v = max(v, max_value(result(board, action)))
    return v


def max_value(board):
    if terminal(board):
        return utility(board)
    v = 2
    for action in actions(board):
        v = min(v, min_value(result(board, action)))
    return v
