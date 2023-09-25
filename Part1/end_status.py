# Write code here to print out the game outcome given a hand value.
hand_value = int(input(""))
if hand_value == 21:
    print("BLACKJACK!")
elif hand_value < 4 or hand_value > 31:
    print("BAD HAND VALUE!")
elif hand_value > 21:
    print("BUST.")
