def is_board_full(board):
  random_list = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
  list_choose = []
  for x in random_list:
    if board[x[0]][x[1]] == "X" or board[x[0]][x[1]] == "O":
      continue
    else:
      list_choose.append(x)
  if len(list_choose) == 0:
    return True
  else:
    return False
  """
  should return True if there are no more empty place on the board,
  otherwise should return False
  """
  pass


if __name__ == "__main__":
  # run this file to test you have implemented correctly the function
  board_1 = [
    ["X", "O", "."],
    ["X", "O", "."],
    ["X", "X", "O"],
  ]
  print(is_board_full(board_1)) # should return False

  board_2 = [
    [".", "O", "O"],
    [".", "O", "X"],
    [".", "X", "X"],
  ]
  print(is_board_full(board_2)) # should return False

  board_3 = [
    ["O", "O", "X"],
    ["O", "X", "O"],
    ["O", "X", "X"],
  ]
  print(is_board_full(board_3)) # should return True