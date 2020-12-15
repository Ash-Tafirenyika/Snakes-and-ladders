# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 01:03:25 2018

@author: Ashy
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 14:36:23 2018

@author: Ashy

"""
from random import randint
input('''         
         *********************************************************************
         *       SNAKES AND LADDERS                                          *
         *                                                                   *
         *       Rules of the game                                           *
         *       ##########################                                  *
         *       1. Allows 2 players to play at a time.                    *
         *       2. Allows Entering of player names.                                      *
         *       3. Has options for dice is rolled automatically through a random process.   *
         *********************************************************************                                                                    *
                    \n\nPress Enter To start game >>>>>  ''') 
input("Enter Setings :")
snake_squares = {16: 4, 33: 20, 48: 24, 62: 56, 78: 69, 94: 16}
ladder_squares = {3: 12, 7: 23, 20: 56, 47: 53, 60: 72, 80: 94}

user = input("Enter dice numbers manualy ,Yes? No? , type yes if so or no if you want to use inbuilt dice : ")
Player1Name = input("What is name of player 1 : ")
Player2Name = input("What is name of player 2 : ")
print(Player1Name,"and",Player2Name,", Welcome to Snakes and Ladders Game.")
input("Press Enter to continue :) ")

P1position = 0
P2position = 0
P1counter = []
P2counter = []

while P1position <= 100 and P2position <= 100:
    if user != "" and user == 'yes':
        number = int(input(" Enter Rolled dice number : "))
        while number not in range(1,6):
            print("Dice rolled number should greater than or equal to 1 and less than or equal to 6")
        user = 'yes'
    elif user != "" and user =='no':
        number = randint(1, 6)
        number2 = randint(1,6)
        user = 'no'
    if P1position >= 100:
        print(Player1Name,"\n wins!!!!!!!!!! ,Sorry", Player2Name," you loose better luck next time ^_^ ")
        break
    elif P2position >= 100:
        print(Player2Name,"\n wins!!!!!!!!!! ,Sorry", Player1Name," you loose better luck next time ^_^ ")
        break
    else:
        
        input(Player1Name + " Roll dice : ")
        print("Rolled : ", number)
        print(Player1Name," you were currently on square  : ",P1position)
        P1position = P1position + number
        print(Player1Name," you are now on square  : ",P1position)    
        if P1position in snake_squares:
             P1position = snake_squares[P1position]
             print(Player1Name," got bitten by a snake and is now on square : ",P1position)
        elif P1position in ladder_squares:
             P1position = ladder_squares[P1position]
             print(Player1Name,"climbed a ladder and is now on square : ",P1position)
       
        if P1position == 100:
            print("Player 1 wins!!!!!!!!!! ,Sorry player 2 you loose better luck next time ^_^ ")
            P1counter += 1
            break
        else:
            
            input(Player2Name + " Roll dice : ")
            print("Rolled : ", number2)
            print(Player2Name," you were currently on square  : ",P2position)
            P2position += number2
            print(Player2Name," you are now on square  : ",P2position)
            if P2position in snake_squares:
                P2position = snake_squares[P2position]
                print(Player2Name,"got bitten by a snake and is now on square : ",P2position)
            
            elif P2position in ladder_squares:
                P2position = ladder_squares[P2position]
                print(Player2Name,"climbed a ladder and is now on square : ",P2position)
        
            if P2position == 100:
                print("Player 2 wins!!!!!!!!!! ,Sorry player 1 you loose better luck next time ^_^ ")
                i += 1
                P2counter.append(i)
                break
           
        
print("\n\t\t\t\t\t GAME OVER ")
repeat()
