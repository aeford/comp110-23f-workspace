"""Practice with while loops using low value string"""

cards: str = "5235"

#look at each number in the string
card_idx: int = 0
low_card: int = int(cards[0])
while card_idx < 4:
    #check if current card is less than low card
    current_card: int = int(cards[card_idx])
    if (current_card < low_card):
        #update low card value to current
        low_card = current_card
    card_idx = card_idx + 1
print(low_card)