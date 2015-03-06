# usr/bin/python3
# Program Name: Challenge_1.py
# Author: Luke Gosnell
# Contributors: Tom Morrissey
# Date: 2/24/2015

import random
import time

""" A playing card. """
RANKS = ["A", "2", "3", "4", "5", "6", "7",
        "8", "9", "10", "J", "Q", "K"]
SUITS = ["c", "d", "h", "s"]

random.choice(RANKS)
random.choice(SUITS)

print(""" Welcome to War! Battle your foe!
reach 5 points first to win!
""")

player1 = input("Enter Player 1: ")
player2 = input("Enter Player 2: ")
player1Amount = 0
player2Amount = 0

while player1Amount < 5 and player2Amount < 5:
    print(player1, "press enter to draw a card.")
    input("")
    print(player1, "draws a card!")
    print("")
    player1CardIndex = random.randrange(len(RANKS))
    player1Suit = random.choice(SUITS)
    player1Card = RANKS[player1CardIndex] + player1Suit
    print(player2, "press enter to draw a card.")
    input("")
    print(player2, "draws a card!")
    print("")
    player2CardIndex = random.randrange(len(RANKS))
    player2Suit = random.choice(SUITS)
    player2Card = RANKS[player2CardIndex] + player2Suit

    print(player1 + ": ", player1Card)
    print(player2 + ": ", player2Card)
    print("")
    
    if player1CardIndex > player2CardIndex:
        print(player1, "wins!")
        player1Amount = player1Amount + 1
    elif player2CardIndex > player1CardIndex:
            print(player2, "wins!")
            player2Amount = player2Amount + 1
    else:
        print("Tie!")
    print("Press enter to continue to the next round.")
    input("")

if player1Amount > 4:
    print(player1, "is the champion!")
elif player2Amount > 4:
    print(player2, "is the champion!")

            
    

    




    

