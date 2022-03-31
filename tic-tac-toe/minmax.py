from function6 import get_winning_player
from function7 import is_board_full

def minmax(board, currentplayer):
    best = float("-inf")
    for a in range(0, 3):
        for b in range(0, 3):
            if board[a][b] == ".":
                board[a][b] = "O"
                score = minmax2(board, currentplayer)
                board[a][b] = "."
                if score > best:
                    move = (a, b)
                    best = score
    return move


def minmax2(board, currentplayer):
    if get_winning_player(board) == "O":
        return 1
    elif get_winning_player(board) == "X":
        return -1
    elif is_board_full(board):
        return 0

    if currentplayer == "X":
        currentplayer = "O"
        best = float("-inf")
        for a in range(0, 3):
            for b in range(0, 3):
                if board[a][b] == ".":
                    board[a][b] = "O"
                    score = minmax2(board, currentplayer)
                    board[a][b] = "."
                    best = max(best, score)
        return best

    if currentplayer == "O":
        currentplayer = "X"
        best = float("inf")
        for a in range(0, 3):
            for b in range(0, 3):
                if board[a][b] == ".":
                    board[a][b] = "X"
                    score = minmax2(board, currentplayer)
                    board[a][b] = "."
                    best = min(best, score)
        return best