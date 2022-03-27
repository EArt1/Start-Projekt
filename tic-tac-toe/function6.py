def get_winning_player(board):
    A1, A2, A3 = board[0]
    B1, B2, B3 = board[1]
    C1, C2, C3 = board[2]
    player = ["X", "O"]
    for i in player:
        if board[0].count(i) == 3:
            return i
        elif board[1].count(i) == 3:
            return i
        elif board[2].count(i) == 3:
            return i
        elif i == A1 and i == B1 and i == C1:
            return i
        elif i == A2 and i == B2 and i == C2:
            return i
        elif i == A3 and i == B3 and i == C3:
            return i
        elif i == A1 and i == B2 and i == C3:
            return i
        elif i == A3 and i == B2 and i == C1:
            return i
    return None


"""
Should return the player that wins based on the tic tac toe rules.
If no player has won, than "None" is returned.
"""
pass


if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    board_1 = [
      ["X", "O", "."],
      ["X", "O", "."],
      ["X", "X", "O"],
    ]
    print(get_winning_player(board_1))  # should return "X"

    board_2 = [
      ["X", "O", "O"],
      ["X", "O", "."],
      ["O", "X", "X"],
    ]
    print(get_winning_player(board_2))  # should return "O"

    board_3 = [
      ["O", "O", "."],
      ["O", "X", "."],
      [".", "X", "."],
    ]
    print(get_winning_player(board_3))  # should return None