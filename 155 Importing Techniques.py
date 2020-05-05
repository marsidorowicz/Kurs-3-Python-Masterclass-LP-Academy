import blackjack
g = sorted(globals())

for x in g:
    print(x)

blackjack.deal_card(blackjack.dealer_card_frame)
blackjack.play()
# print(__name__)
# blackjack.play()
# print(blackjack.cards)