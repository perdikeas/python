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


def get_random_word():
    word_index=random.randint(0,len(words)-1)
    return words[word_index]

def prompt_the_user_to_guess():
    print('Guess a  letter (you have {} tries left)'.format(tries_left))
    guess=str(input())

    if guess in secret_word:
        handle_correct_guess(guess)
    else:
        handle_wrong_guess(guess)

def handle_correct_guess(x):
    global word_found
    indices=[m.start() for m in re.finditer(x,secret_word)]
    for index in indices:
        word_found=word_found[:index]+secret_word[index]+word_found[index+1:]

def handle_wrong_guess(y):
    global tries_left
    tries_left-=1
    print('This letter is not in the secret word,you fucked up')



def print_current_hanging_state():
    print(HANGMAN_PICS[len(HANGMAN_PICS)-1-tries_left])

def should_game_continue():
    print('\n\n\tThe secret word was {} , better luck next time'.format(secret_word))
    if str(input('\n\n\tDo u wanna play again,yes or no?')).startswith('y')==True:
        initialize_game()
        return True
    else:
        return False



secret_word = None
tries_left = None
word_found = None
word_found_displayed_to_user=None
def initialize_game():
    global secret_word
    global tries_left
    global word_found
    secret_word=get_random_word()
    tries_left=len(HANGMAN_PICS)
    word_found='_'*len(secret_word)


def print_word_found_so_far():
    print(" ".join(list(word_found)))

initialize_game()
while True:
    while tries_left!=0 and word_found!=secret_word:
        print("\tThis is Hangman, caution: all the secret words are animals")
        print("\n\n\t")
        print_current_hanging_state()
        print("\n\n\t")
        print_word_found_so_far()
        print("\n\n\t")
        prompt_the_user_to_guess()

    if  (not should_game_continue()):
        break
