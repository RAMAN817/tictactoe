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
    xcount = sum(x.count(X) for x in board)
    ocount = sum(o.count(O) for o in board)
    return O if xcount > ocount else X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_action = set()

    for i in range(0 , len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == EMPTY:
                possible_action.add((i , j))
    return possible_action



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #creaating a new board without modifying old one
    result = copy.deepcopy(board)
    result[action[0]][action[1]] = player(board)
    return result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #we have to check rows , colunms and diagnols too

    #checking rows
    if all(i == board[0][0] for i in board[0]):
        return board[0][0]
    elif all(i == board[1][0] for i in board[1]):
        return board[1][0]
    elif all(i == board[2][0] for i in board[2]):
        return board[2][0]

    #checking columns
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        return board[0][0]
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        return board[0][1]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        return board[2][2]

    #checking diagnols
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]
    #if nothing returns none

    else:
        return None

def terminal(board):
    if winner(board) is not None or not any(EMPTY in row for row in board):
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0

def minimax(board):
    if terminal(board):
        return  utility(board),None
    else:
        if player(board) == X:
            value , move= max_value(board , float('-inf'), float('inf'))
            return move
        else:
            value, move = min_value(board , float('-inf'), float('inf'))
            return move

def max_value(board, alpha, beta):
    if terminal(board):
        return utility(board), None  # Return a tuple (score, move)
    v = float('-inf')
    move = None
    for action in actions(board):
        eval, _ = min_value(result(board, action), alpha, beta)  # Unpack expected tuple
        if eval > v: # -1 or 1 or 0 > -inf
            v = eval  # -1 or 1 or 0 = eval
            move = action
        alpha = max(alpha, v) #  v= alpha
        if v >= beta: # -1 or 1 or 0 >= inf
            break
    return v, move  # Return a tuple (score, move)


def min_value(board, alpha, beta):
    if terminal(board):
        return utility(board), None  # Return a tuple (score, move)
    v = float('inf')
    move = None
    for action in actions(board):
        eval, _ = max_value(result(board, action), alpha, beta)  # Unpack expected tuple
        if eval < v: # -1 or 1 or 0 < inf
            v = eval
            move = action
        beta = min(beta, v)
        if v <= alpha:
            break
    return v, move  # Return a tuple (score, move)



