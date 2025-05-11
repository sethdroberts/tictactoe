import random

POSSIBLE_WINNING_ROWS = (
        (1, 2, 3),  # top row of board
        (4, 5, 6),  # center row of board
        (7, 8, 9),  # bottom row of board
        (1, 4, 7),  # left column of board
        (2, 5, 8),  # middle column of board
        (3, 6, 9),  # right column of board
        (1, 5, 9),  # diagonal: top-left to bottom-right
        (3, 5, 7),  # diagonal: top-right to bottom-left
    )

def count_markers_for(squares, player, keys):
    markers = [squares[str(key)] for key in keys]
    return markers.count(player)

def three_in_a_row(squares, player, row):
    return count_markers_for(squares, player, row) == 3

def is_winner(squares, player):
    for row in POSSIBLE_WINNING_ROWS:
        if three_in_a_row(squares, player, row):
                return True
        return False

def is_unused(square):
    return square == " "
    
def unused_squares(squares):
    return [key for key, value in squares.items() if is_unused(value)]

def someone_won(squares):
    return is_winner(squares, 'X') or is_winner(squares, 'O')

def board_full(squares):
    return len(unused_squares(squares)) == 0
    
def game_over(squares):
    return board_full(squares) or someone_won(squares)

def computer_move(squares):
    return random.choice(unused_squares(squares))
