# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
from blackjack_helper import *

# Write all of your part 3 code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.

#user turn

user_hand_value = draw_starting_hand("YOUR")
user_option = ""
while user_hand_value < 21:
    user_option = input("You have {}. Hit (y/n)? ".format(user_hand_value))
    if user_option == 'n':
        break
    elif user_option != 'y':
        print("Sorry I didn't get that.")
    else:
        user_hand_value += draw_card()
print_end_turn_status(user_hand_value)


#dealers turn
dealer_hand_value = draw_starting_hand("DEALER")
while dealer_hand_value < 17:
    print("Dealer has {}.".format(dealer_hand_value))
    dealer_hand_value += draw_card()
print_end_turn_status(dealer_hand_value)

#Result

print_end_game_status(user_hand_value, dealer_hand_value)