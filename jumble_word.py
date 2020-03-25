# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 23:02:06 2020

@author: Biswaraj

Jumbled Words Game
"""
import random

def choose():
    word_list = ['rifle', 'scarecrow', 'battle', 'bad', 'fearful', 'tricky', 'long-term', 'wanting', 'abrasive', 'thrill', 'interfere', 'protective', 'recess', 'ambitious', 'belief' ,'breath']
    pick = random.choice(word_list) # choice is a built in function which will choose a word from the list.
    return pick

def jumble(pick):
    convert_to_list = list(pick) # convert the word to a list so as to use random.shuffle function on it.
    random.shuffle(convert_to_list)
    jumbled_word = ''.join(convert_to_list) # joins the items in list with no space
    return jumbled_word

def thankyou(player1,player2,player1_points,player2_points):
    print('\n\tGame Summary : ')
    print('\n\t{}\'s points is {} and {}\'s points is {}'.format(player1,player1_points,player2,player2_points))
    print('\n\tThankYou for Playing.')
    print('\n\tHave a Nice Day !!😊😊')

def play():
    player1 = input('Player 1, Please Enter Your name:\t')
    player2 = input('Player 2, Please Enter Your name:\t')
    player1_points = 0
    player2_points = 0
    turn = 0
    
    while True:
        # Computer Task
        picked_word = choose()
        # Create Question
        question = jumble(picked_word)
        print(f'\nThe Jumbled word is : {question}')
        
        # Player 1 Turn in even no. and player 2 turnb in odd no.'s .
        
        # PLayer 1
        if turn%2 == 0:
            print('\n{}\'s Turn : '.format(player1))
            answer = input('What\'s in your mind : ')
            if answer.lower() == picked_word.lower():
                player1_points += 10
                print('Correct Answer!!')
                print('\nYou get 10 Points!! \nNow, Your Score is : ', player1_points)
            else:
                print('\nBetter Luck Next Time, The answer is : ',picked_word)
            
            continue_or_not = int(input('Continue Game ? (Press 1 to continue and 0 to stop) : '))
            if continue_or_not == 0:
                thankyou(player1,player2,player1_points,player2_points)
                break
        # Player 2
        else:
            print('\n{}\'s Turn : '.format(player2))
            answer = input('What\'s in your mind : ')
            if answer.lower() == picked_word.lower():
                player2_points += 10
                print('\nCorrect Answer!!')
                print('\nYou get 10 Points!! \nNow, Your Score is : ', player2_points)
            else:
                print('\nBetter Luck Next Time, The answer is : ',picked_word)
            
            continue_or_not = int(input('Continue Game ? (Press 1 to continue and 0 to stop) : '))
            if continue_or_not == 0:
                thankyou(player1,player2,player1_points,player2_points)
                break
        turn += 1
            
play()





