def get_empty_board():
    play_board = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
    return play_board


'''
    Should return a list with 3 sublists.
    Each sublist should contain 3 time the "." character
    '''


if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    board = get_empty_board()
    print(board)