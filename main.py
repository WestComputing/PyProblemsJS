cards = [card for card in range(10, 100)]
hand = []
while cards:
    card = cards.pop()
    complement = 100 - card
    complement_index = None
    try:
        complement_index = hand.index(complement)
        continue
    except ValueError:
        pass
    try:
        complement_index = cards.index(complement)
        cards.pop(complement_index)
    except ValueError:
        pass
    hand.append(card)
print(hand)
print(len(hand), "cards")
