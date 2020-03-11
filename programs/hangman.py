#!/usr/bin/env python3
import random
import re
HANGMAN_PICS=['''
  +---+
      |
      |
      |
     ===''', '''
    +---+
    0   |
        |
        |
       ===''','''
    +---+
    0   |
    |   |
        |
       ===''','''
    +---+
    0   |
   /|   |
        |
       ===''','''
    +---+
    0   |
   /|\  |
        |
       ===''','''
    +---+
    0   |
   /|\  |
   /    |
       ===''','''
    +---+
    0   |
   /|\  |
   / \  |
       ===''']
words='''ant,baboon,badger,beatle,cat,cobra,coala,caiman,cougar,cayote,deer,dog,donkey,eahle,ferret,fox,frog,goat,goose,hawk,
lion,lizard,llama,mole,monkey,moose,mouse,mule,newt,otter,owl,panda,parrot,python,rabbit,raven,rhino,salmon,shark,snake,spider
,tiger,toad,turkey,turkey,weasel,whale,wolf,urangutang,zebra'''.split(',')


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



def get_random_word():
    wordIndex=random.randint(0,len(words)-1)
    word= words[wordIndex]
    return word
#state


secret_word=None
word_found=None
tries_left=None


def initialize_game_state():
    global secret_word, word_found, tries_left
    secret_word=get_random_word()
    print(secret_word)
    word_found='_'*len(secret_word)
    tries_left=len(HANGMAN_PICS)



def print_current_hanging_state():
    print (HANGMAN_PICS[len(HANGMAN_PICS)-tries_left])

def print_word_found():
    print ('     ' + ' '.join(list(word_found)))
    print('\n\n')

def manage_correct_guess():
    global guess
    global secret_word
    global word_found
    indices=[guess.start() for guess in re.finditer(guess,secret_word)]
    for i in indices:
        word_found=word_found[:i]+secret_word[i]+word_found[i+1:]

def manage_wrong_guess():
    global tries_left
    tries_left-=1
    print(Color.RED+Color.BOLD+Color.UNDERLINE+'You fucked up'+Color.END)

def manage_guess(guess):
    global secret_word
    if guess in secret_word:
        manage_correct_guess()
    else:
        manage_wrong_guess()

def get_guess():
    print('Guess a letter (you have {}{}{} guesses left)'.format(Color.CYAN, tries_left, Color.END))
    while (True):
        guess=input()
        if len(guess)!=1 or guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('I asked u to print a letter u moron')
        else:
            return guess



def end_game_or_start_new():
    print('Do you want to play again, yes or no?')
    b=input()
    if b.startswith('y'):
        initialize_game_state()



print('This is Hangman')
initialize_game_state()
while (tries_left > 0):
    print_current_hanging_state()
    print_word_found()
    guess = get_guess()
    manage_guess(guess)
    if tries_left==0:
        print('You lost,the secret word was {} '.format(secret_word))
        end_game_or_start_new()

    if word_found==secret_word:
        print('You won, congratulations! the secret word was \'{}\' - you had {} tries left'.format(secret_word, tries_left))
        end_game_or_start_new()
