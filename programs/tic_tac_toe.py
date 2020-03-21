#!/usr/bin/env python3
board=[None, '1','2','3','4','5','6','7','8','9']

import random
letters=['X','O']
player_letter=None
computer_letter=None


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
    return (board[space]!='X' and board[space]!='O')

assign_letters()

def make_move(board,letter,move):
    board[move]=letter
    draw_board(board)


def is_board_full(board):
    for i in board:
        if i !=' ':
            return False
    return True

def get_player_move():

     print('Make a move(1-9)')
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
    assert False, "you're not supposed to ever reach this line"
    +" (function 'is_board_full' should have already"
    +" checked for this condition)"


def ask_to_play_again():
    return input('Do you want to play again, yes or no ? ').startswith('y')


game_over=False

assign_letters()
turn=get_turn_order(letters)
draw_board(board)
while game_over==False:
    if turn==player_letter:
        print('human turn')
        print("\n\n")
        move=get_player_move()
        print("\n\n")

        make_move(board,player_letter,move)

        if is_winner(board,player_letter):
            print('You beat the computer , congratulations!')
            ask_to_play_again()

        elif is_board_full(board):
            ask_to_play_again()
        else:
            turn=computer_letter
    else:
        print('AI turn')
        print("\n\n")
        move=get_optimal_computer_move(board)
        make_move(board,computer_letter,move)
        if is_winner(board,computer_letter):
            print("\n\n")
            print('The computer has beaten you')
            ask_to_play_again()
        elif is_board_full(board):
            ask_to_play_again()
        else:
            turn=player_letter
