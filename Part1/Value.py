card_value = int(input(""))
if(card_value == 1):
    print("Your hand value is 11.")
elif (card_value == 11 or card_value == 12 or card_value == 13):
    print("Your hand value is 10.")
elif (card_value > 1 and card_value < 11):
    print("Your hand value is " + str(card_value) + ".")
else:
    print("BAD CARD")