"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None
BOARD_SIZE = 3


def initial_state():
    """
    Returns starting state of the board.
    """
    # return [[EMPTY, EMPTY, EMPTY],
    #         [EMPTY, EMPTY, EMPTY],
    #         [EMPTY, EMPTY, EMPTY]]
    return [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


def player(board):
    """
    Returns player who has the next turn on a board.
    In the initial game state, X gets the first move.
    """
    # raise NotImplementedError
    num_x = sum(row.count(X) for row in board)
    num_o = sum(row.count(O) for row in board)
    return X if num_x == num_o else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # raise NotImplementedError
    return {
        (i, j) for i in range(BOARD_SIZE) for j in range(BOARD_SIZE)
        if board[i][j] == EMPTY
    }


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # raise NotImplementedError
    if terminal(board):
        # print("ERROR BOARD:", board)
        # print("WINNER:", winner(board))
        # print("ACTIONS:", actions(board))
        raise ValueError("Invalid move: The game is already over.")
    if action not in actions(board):
        raise ValueError("Invalid move: The cell is not empty.")

    state = [row.copy() for row in board]
    state[action[0]][action[1]] = player(board)
    return state


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # raise NotImplementedError
    # Check rows and columns
    for i in range(BOARD_SIZE):
        if board[i][0] is not EMPTY and all(
            board[i][j] == board[i][0] for j in range(BOARD_SIZE)
        ):
            return board[i][0]

        if board[0][i] is not EMPTY and all(
            board[j][i] == board[0][i] for j in range(BOARD_SIZE)
        ):
            return board[0][i]

    # Check diagonal
    if board[0][0] is not EMPTY and all(
        board[i][i] == board[0][0] for i in range(BOARD_SIZE)
    ):
        return board[0][0]

    # Check anti-diagonal
    if board[0][BOARD_SIZE - 1] is not EMPTY and all(
        board[i][BOARD_SIZE - 1 - i] == board[0][BOARD_SIZE - 1]
        for i in range(BOARD_SIZE)
    ):
        return board[0][BOARD_SIZE - 1]


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # raise NotImplementedError
    return winner(board) is not None or not actions(board)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # raise NotImplementedError
    game_winner = winner(board)
    if game_winner == X:
        return 1
    if game_winner == O:
        return -1
    return 0


def max_value(board):
    if terminal(board):
        return utility(board)
    return max(min_value(result(board, action)) for action in actions(board))


def min_value(board):
    if terminal(board):
        return utility(board)
    return min(max_value(result(board, action)) for action in actions(board))

    
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # raise NotImplementedError
    if terminal(board):
        return None

    available_actions = actions(board)
    
    # If it's X's turn, find the action that maximizes the minimum value
    if player(board) == X:
        best_action = None
        best_value = -math.inf
        for action in available_actions:
            value = min_value(result(board, action))
            if value > best_value:
                best_action = action
                best_value = value
        return best_action

    # If it's O's turn, find the action that minimizes the maximum value
    best_action = None
    best_value = math.inf
    for action in available_actions:
        value = max_value(result(board, action))
        if value < best_value:
            best_action = action
            best_value = value
    return best_action
