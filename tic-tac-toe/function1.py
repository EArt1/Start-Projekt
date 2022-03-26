def get_menu_option():
  while True:
    how_play = input("""
    What do you want? Select a number from 1 to 4.
    1. Human vs Human
    2. Random AI vs Random AI
    3. Human vs Random AI
    4. Human vs Unbeatable AI
     """)
    try:
      how_play = int(how_play)
      if how_play in [1, 2, 3, 4]:
        return how_play
      else:
        print("Please only numbers from 1 to 4.")
    except ValueError:
      print("Please only numbers from 1 to 4.")

'''
  Should print a menu with the following options:
  1. Human vs Human
  2. Random AI vs Random AI
  3. Human vs Random AI
  4. Human vs Unbeatable AI

  The function should return a number between 1-4.
  If the user will enter invalid data (for example 5), than a message will appear
  asking to input a new value.
  '''


if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    option = get_menu_option()
    print(option) # if the user selected 1, it should print 1