#!/usr/bin/env python3

import random


board_initial_state=[None, '1','2','3','4','5','6','7','8','9']
board=None


class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


letters=[Color.CYAN+'X'+Color.END
,Color.RED+'O'+Color.END]
player_letter=None
computer_letter=None


def re_initialize_board():
    global board
    board=board_initial_state.copy()

def draw_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-+-+-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-+-+-')
    print(board[1]+'|'+board[2]+'|'+board[3])


def is_odd(a):
    return a%2==1

def get_board_copy(board):
    return [i for i in board]

def replace_letter_in_board_copy(letter,board_copy,move):
    board_copy[move]=letter

def assign_letters():
    global player_letter,computer_letter
    player_letter=letters[random.randint(0,1)]
    computer_letter=letters[0 if player_letter==letters[1] else 1]


def get_turn_order(list):
    plays_first=list[random.randint(0,1)]
    return plays_first


def is_winner(bo,letter):
    return ((bo[7]==bo[8]==bo[9]==letter) or
            (bo[4]==bo[5]==bo[6]==letter) or
            (bo[1]==bo[2]==bo[3]==letter) or
            (bo[7]==bo[5]==bo[3]==letter) or
            (bo[9]==bo[5]==bo[1]==letter) or
            (bo[1]==bo[4]==bo[7]==letter) or
            (bo[2]==bo[5]==bo[8]==letter) or
            (bo[3]==bo[6]==bo[9]==letter))

def is_space_free(board,space):
    return (board[space]!=letters[0] and board[space]!=letters[1])



def make_move(board,letter,move):
    board[move]=letter
    draw_board(board)


def is_board_full(board):
    for i in board:
        if i!=player_letter and i!=board[0] and i!=computer_letter:
            return False
    return True


def get_player_move():
    if player_letter==letters[0]:
        print(Color.CYAN+'Make a move(1-9)'+Color.END)
    else:
        print(Color.RED + 'Make a move(1-9)'+Color.END)
    choice = int(input())
    while (not is_space_free(board,choice)):
        print('Make another move, this space is taken')
        choice = int(input())
    return choice


def get_optimal_computer_move(board):
    global computer_letter
    center=5
    for i in range(1,10):
        board_copy=get_board_copy(board)
        if is_space_free(board_copy,i):
            replace_letter_in_board_copy(computer_letter,board_copy,i)
            if is_winner(board_copy,computer_letter):
                return i
    for i in range(1,10):
        board_copy=get_board_copy(board)
        if is_space_free(board_copy,i):
            replace_letter_in_board_copy(player_letter,board_copy,i)
            if is_winner(board_copy,player_letter):
                return i

    if is_space_free(board_copy,center):
        return center

    for i in range(1,10):
        if is_odd(i) and is_space_free(board,i):
            return i

    for i in range(1,10):
        if is_space_free(board_copy,i):
            return i





def ask_to_play_again():
    global game_over
    global board
    print('Do you want to play again?')
    if input().startswith('y'):
        re_initialize_board()
    else:
        game_over=True

def draw_dected():
    print('It was a draw this time, nice one')
    ask_to_play_again()

# execution starts here!

game_over=False
re_initialize_board()
assign_letters()
turn=get_turn_order(letters)
draw_board(board)
while game_over==False:
    if turn==player_letter:
        print("\n\n\n")
        move=get_player_move()
        make_move(board,player_letter,move)
        turn=computer_letter
    else:
        computer_color = Color.CYAN if computer_letter==letters[0] else Color.RED
        print("\n\n\n")
        print(computer_color+'AI turn'+Color.END)
        move=get_optimal_computer_move(board)
        make_move(board,computer_letter,move)
        turn=player_letter
    if is_winner(board,computer_letter) or is_winner(board,player_letter):
        msg = 'You beat the computer, congratulations!' if  is_winner(board,player_letter) else 'The AI destroyed you due to superior intellect'
        print(msg)
        ask_to_play_again()
    elif is_board_full(board):
        draw_dected()
