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
    c=0
    for L in board:
        for d in L:
            if d is not None:
                c=c+1
    if c%2==0 or c==0:
        return X
    else:
        return O

    """
    Returns player who has the next turn on a board.
    """
    
   


def actions(board):
    A=set()
    for i in range(3):
        for j in range(3):
            if board[i][j]==None:
                A.add((i,j))
    return A
    """
    Returns set of all possible actions (i, j) available on the board.
    """
   


def result(board, action):
    B=copy.deepcopy(board)
    if action not in actions(board):
        raise Exception("Not a valid action")
    else:
        (i,j)=action
        B[i][j]=player(board)
    return B
    """
    Returns the board that results from making move (i, j) on the board.
    """
   


def winner(board):
    for i in range(3):
        if board[i][0]==board[i][1] and board[i][0]==board[i][2]:
            return board[i][0]
    for j in range(3):
        if board[0][j]==board[1][j] and board[0][j]==board[2][j]:
            return board[0][j]
    if board[0][0]==board[1][1] and board[0][0]==board[2][2]:
        return board[0][0]
    if board[0][2]==board[1][1] and board[0][2]==board[2][0]:
        return board[0][2]
    else:
        return None
    """
    Returns the winner of the game, if there is one.
    """
  


def terminal(board):
    c=0
    for L in board:
        for d in L:
            if d==None:
                c=c+1
    if winner(board) is not None or c==0:
         return True
    """
    Returns True if game is over, False otherwise.
    """
  


def utility(board):
    if terminal(board)==True:
        if winner(board)==X:
            return 1
        if winner(board)==O:
            return -1
        else:
            return 0

    
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
def MAX_value(board):
    if terminal(board)==True:
        return utility(board)
    else:
        L1=[]
        L2=list(actions(board))
        for action in L2:
            b=result(board, action)
            L1=L1+[MIN_value(b)]
        return max(L1)
        
        
    
def MIN_value(board):
    if terminal(board)==True:
        return utility(board)
    else:
        L3=[]
        L4=list(actions(board))
        for action in L4:
            b=result(board, action)
            L3=L3+[MAX_value(b)]
        
        return min(L3)
        
def minimax(board):
    L=actions(board)
    if terminal(board)==True:
        return None
    else:
        if player(board)==X:
            for action in L:
                if MIN_value(result(board, action))==MAX_value(board):
                    return action
                
           
        else:
            for action in L:
                if MAX_value(result(board, action))==MIN_value(board):
                    return action
            
    """
    Returns the optimal action for the current player on the board.
    """
 