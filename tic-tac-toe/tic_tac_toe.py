from function0 import display_board
from function1 import get_menu_option
from function2 import get_empty_board
from function3 import get_human_coordinates
from function4 import get_random_ai_coordinates
from function5 import get_unbeatable_ai_coordinates
from function6 import get_winning_player
from function7 import is_board_full
import time


HUMAN_VS_HUMAN = 1
RANDOM_AI_VS_RANDOM_AI = 2
HUMAN_VS_RANDOM_AI = 3
HUMAN_VS_UNBEATABLE_AI = 4


def main():
    while True:
        game_mode = get_menu_option()
        board = get_empty_board()
        # is_game_running = True
        pause_time = 2
        if game_mode == 1:
            while True:
                display_board(board)
                print("It is X turn.")
                current_player = "X"
                x, y = get_human_coordinates(board, current_player)
                board[x][y] = current_player
                winning_player = get_winning_player(board)
                if winning_player == current_player:
                    break
                elif is_board_full(board):
                    break
                display_board(board)
                print("It is O turn.")
                current_player = "O"
                x, y = get_human_coordinates(board, current_player)
                board[x][y] = current_player
                winning_player = get_winning_player(board)
                if winning_player == current_player:
                    break
                elif is_board_full(board):
                    break
        elif game_mode == 2:
            while True:
                display_board(board)
                print("It is X turn.")
                time.sleep(pause_time)
                current_player = "X"
                x, y = get_random_ai_coordinates(board, current_player)
                board[x][y] = current_player
                winning_player = get_winning_player(board)
                if winning_player == current_player:
                    break
                elif is_board_full(board):
                    break
                display_board(board)
                print("It is O turn.")
                time.sleep(pause_time)
                current_player = "O"
                x, y = get_random_ai_coordinates(board, current_player)
                board[x][y] = current_player
                winning_player = get_winning_player(board)
                if winning_player == current_player:
                    break
                elif is_board_full(board):
                    break
        elif game_mode == 3:
            while True:
                display_board(board)
                print("It is X turn.")
                current_player = "X"
                x, y = get_human_coordinates(board, current_player)
                board[x][y] = current_player
                winning_player = get_winning_player(board)
                if winning_player == current_player:
                    break
                elif is_board_full(board):
                    break
                display_board(board)
                print("It is O turn.")
                time.sleep(pause_time)
                current_player = "O"
                x, y = get_random_ai_coordinates(board, current_player)
                board[x][y] = current_player
                winning_player = get_winning_player(board)
                if winning_player == current_player:
                    break
                elif is_board_full(board):
                    break
        elif game_mode == 4:
            while True:
                display_board(board)
                print("It is X turn.")
                current_player = "X"
                x, y = get_human_coordinates(board, current_player)
                board[x][y] = current_player
                winning_player = get_winning_player(board)
                if winning_player == current_player:
                    break
                elif is_board_full(board):
                    break
                display_board(board)
                print("It is O turn.")
                time.sleep(pause_time)
                current_player = "O"
                x, y = get_unbeatable_ai_coordinates(board, current_player)
                board[x][y] = current_player
                winning_player = get_winning_player(board)
                if winning_player == current_player:
                    break
                elif is_board_full(board):
                    break
        display_board(board)
        if is_board_full(board):
            print("It is a tie.")
        else:
            print(f"Congratulations {winning_player} you win!")

    # ## TO DO ###
    # in each new iteration of the while loop the program should
    # alternate the value of `current_player` from `X` to `O`
    # current_player = 'X'

    # ## TO DO ###
    # based on the value of the variables `game_mode` and `current_player`
    # the programm should should choose betwen the functions
    # get_random_ai_coordinates or get_umbeatable_ai_coordinates or get_human_coordinates
    # x, y = get_human_coordinates(board, current_player)

    # board[x][y] = current_player

    # ## TO DO ###
    # based on the values of `winning_player` and `its_a_tie` the program
    # should either stop displaying a winning/tie message
    # OR continue the while loop
    # winning_player = get_winning_player(board)
    # its_a_tie = is_board_full(board)


if __name__ == "__main__":
    main()
