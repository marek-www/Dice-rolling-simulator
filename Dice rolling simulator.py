# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 15:46:45 2020

@author: Marek
"""

import random

h = 0
c = 0

def game_set():
    
    while True:
        
        try:
            rolls = int(input("How many rolls?\n"))
            break
        except:
            print('Not a number! Try again!')
    return rolls

def generate_number():
    
    return random.randrange(1, 7)

def find_winner(human, computer):
    
    global h, c
    if human > computer:
        h += 1
        print(f'You win! Total score is: {h} : {c}\n')        
    elif human == computer:
        print(f"It's a tie! Total score is: {h} : {c}\n")
    else:
        c += 1
        print(f'You loose! Total score is: {h} : {c}\n')

      
def game():
    
    duels = game_set()
    
    while duels > 0:
        player = generate_number()
        opponent = generate_number()
        print(f'Your number: {player}\nComputers number: {opponent}')
        find_winner(player, opponent)
        duels -= 1
    if h > c:
        print('You won the duel!')
    elif h ==c:
        print("You tied the duel!")  
    else:
        print('You lost duel!')

game()