""" This class is responsible for
- storing all information about current state of a chess game
- evaluate valid moves
- keep a move log
"""


class GameState:
    def __init__(self):
        # The board is 8x8 list, each element of list has 2 characters
        # The 1st character represents color (b)lack or (w)hite
        # The 2nd character represents type of piece P,K,Q,R,B,N
        # A List of Lists
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--", ],
            ["--", "--", "--", "--", "--", "--", "--", "--", ],
            ["--", "--", "--", "--", "--", "--", "--", "--", ],
            ["--", "--", "--", "--", "--", "--", "--", "--", ],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]
        self.whiteToMove = True
        self.moveLog = []
