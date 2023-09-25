# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
# Use randint to generate random cards. 
from random import randint
# Write all of your part 2A code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.
hand_value = 0
count = 0

while count <2:
    card_drawn = randint(1, 13)
    if(card_drawn == 1):
        print("Drew an Ace")
    elif(card_drawn == 8):
        print("Drew an 8")
    elif(card_drawn == 11):
        print("Drew a Jack")
    elif(card_drawn == 12):
        print("Drew a Queen")
    elif(card_drawn == 13):
        print("Drew a King")
    else:
        print("Drew a " + str(card_drawn))


    if card_drawn == 11 or card_drawn == 12 or card_drawn == 13:
        card_value = 10
    elif card_drawn == 1:
        card_value = 11
    else:
        card_value = card_drawn
    
    hand_value += card_value
    count += 1
if hand_value < 17:
    print("Dealer has {}.".format(hand_value))

while hand_value < 17:
    card_drawn = randint(1, 13)
    if(card_drawn == 1):
        print("Drew an Ace")
    elif(card_drawn == 8):
        print("Drew an 8")
    elif(card_drawn == 11):
        print("Drew a Jack")
    elif(card_drawn == 12):
        print("Drew a Queen")
    elif(card_drawn == 13):
        print("Drew a King")
    else:
        print("Drew a " + str(card_drawn))


    if card_drawn == 11 or card_drawn == 12 or card_drawn == 13:
        card_value = 10
    elif card_drawn == 1:
        card_value = 11
    else:
        card_value = card_drawn
    
    hand_value += card_value

    if hand_value < 17:
        print("Dealer has {}.".format(hand_value))

if hand_value >= 17:

    if hand_value == 21:
        print("Final hand: 21.")
        print("BLACKJACK!")
    elif hand_value >21:
        print("Final hand: {}.".format(hand_value))
        print("BUST.")
    else:
        print("Final hand: {}.".format(hand_value))
