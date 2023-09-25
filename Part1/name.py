card_choice = int(input(""))

if(card_choice == 1):
    print("Drew an Ace")
elif(card_choice == 8):
    print("Drew an 8")
elif(card_choice == 11):
    print("Drew a Jack")
elif(card_choice == 12):
    print("Drew a Queen")
elif(card_choice == 13):
    print("Drew a King")
elif(card_choice > 1 and card_choice < 11 and card_choice != 8):
    print("Drew a " + str(card_choice))
else:
    print("BAD CARD")