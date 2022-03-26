def get_human_coordinates(board, current_player):
  while True:
    move = []
    play = input("It is you turn. Please write the letter row and the number column (e.g. B1) or quit for ending the \
game.").upper()
    if play == "QUIT":
      exit("I hope you had fun.")
    elif play[0] not in ["A", "B", "C"] or play[1] not in ["1", "2", "3"] or len(play) != 2:
      print("Wrong input.")
    else:
      if play[0] == "A":
        move.append(0)
      elif play[0] == "B":
        move.append(1)
      elif play[0] == "C":
        move.append(2)
      if play[1] == "1":
        move.append(0)
      elif play[1] == "2":
        move.append(1)
      elif play[1] == "3":
        move.append(2)
      move1 = tuple(move)
      if board[move1[0]][move1[1]] == "X" or board[move1[0]][move1[1]] == "O":
        print("This coordinates are already taken.")
      else:
        return move1



"""
  Should return the read coordinates for the tic tac toe board from the terminal.
  The coordinates should be in the format  letter, number where the letter is 
  A, B or C and the number 1, 2 or 3.
  If the user enters an invalid coordinate (like Z0 or 1A, A11, sadfdsaf) 
  than a warning message should appear and the coordinates reading process repeated.
  If the user enters a coordinate that is already taken on the board.
  than a warning message should appear and the coordinates reading process repeated.
  If the user enters the word "quit" in any format of capitalized letters the program
  should stop.
  """


if __name__ == "__main__":
  # run this file to test you have implemented correctly the function
  board_1 = [
    ["X", "X", "."],
    ["X", ".", "."],
    ["X", "X", "."],
  ]
  coordinates = get_human_coordinates(board_1, "X")
  print(coordinates) # the only possible returned value can be (0,2) or (1,1) or (1, 2) or (2,2) because they are the only valid ones