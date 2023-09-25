# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
from random import randint

# Write all of your part 3 code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.
user_turn = True
user_status = ''
dealer_status = ''

while user_turn:
  print('-----------')
  print('YOUR TURN')
  print('-----------')

  user_hand_value = 0
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
      
      user_hand_value += card_value
      count += 1

  user_option = ''

  if user_hand_value < 21:
      while user_option != 'y' and user_option != 'n':
          user_option = input("You have {}. Hit (y/n)? ".format(user_hand_value))
          if user_option != 'y' and user_option != 'n':
              print("Sorry I didn't get that.")
  else:
      if user_hand_value == 21:
          print('Final hand: 21.')
          user_status = 'BLACKJACK'
          print('BLACKJACK!')
      elif user_hand_value >21:
          print('Final hand: {}.'.format(user_hand_value))
          user_status = 'BUST'
          print('BUST.')
  while user_option == 'y' and user_hand_value <21:
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
      
      user_hand_value += card_value
      user_option = ''

      if user_hand_value == 21:
          print('Final hand: 21.')
          user_status = 'BLACKJACK'
          print('BLACKJACK!')
      elif user_hand_value >21:
          print('Final hand: {}.'.format(user_hand_value))
          user_status = 'BUST'
          print('BUST.')
      else:
          while user_option != 'y' and user_option != 'n':
              user_option = input("You have {}. Hit (y/n)? ".format(user_hand_value))
              if user_option != 'y' and user_option != 'n':
                  print("Sorry I didn't get that.")
  if user_option == 'n':
      print("Final hand: {}.".format(user_hand_value))
  user_turn = False

dealer_turn = True

while dealer_turn:
    print('-----------')
    print('DEALER TURN')
    print('-----------')

    dealer_hand_value = 0
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
        
        dealer_hand_value += card_value
        count += 1
    if dealer_hand_value < 17:
        print("Dealer has {}.".format(dealer_hand_value))

    while dealer_hand_value < 17:
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
        
        dealer_hand_value += card_value

        if dealer_hand_value < 17:
            print("Dealer has {}.".format(dealer_hand_value))

    if dealer_hand_value >= 17:

        if dealer_hand_value == 21:
            print("Final hand: 21.")
            dealer_status = 'BLACKJACK'
            print("BLACKJACK!")
        elif dealer_hand_value >21:
            print("Final hand: {}.".format(dealer_hand_value))
            dealer_status = 'BUST'
            print("BUST.")
        else:
            print("Final hand: {}.".format(dealer_hand_value))

    dealer_turn = False

print('-----------')
print('GAME RESULT')
print('-----------')

if user_status == 'BLACKJACK' and dealer_status != 'BLACKJACK':
    print("You win!")

elif user_status != 'BUST' and dealer_status == 'BUST':
    print("You win!")

elif user_status == 'BUST' and dealer_status == 'BUST':
    if user_hand_value < dealer_hand_value:
        print("Dealer wins!")
    elif user_hand_value == dealer_hand_value:
        print("Push.")
    else:
        print("You win!")
elif (user_status == 'BLACKJACK' and dealer_status == 'BLACKJACK') or (user_hand_value == dealer_hand_value):
    print("Push.")

elif user_status == 'BUST' and dealer_status != 'BUST':
    print('Dealer wins!')

elif user_hand_value > dealer_hand_value:
    print("You win!")

elif user_hand_value < dealer_hand_value:
    print("Dealer wins!")


