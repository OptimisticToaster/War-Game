from player import Player
from card import Card
mark = Player()
new_cards = [Card('C', '3'), Card('D', 'Q'), Card('S', '6'), Card('H', 'A'), Card('H', '4'), Card('S', '9'), Card('D', 'A'), Card('C', '10')]
# new_cards = [Card('C', '3')]
mark.add_cards(new_cards)
print(f'Mark has {len(mark)} cards:  {mark}')
# h.remove_card_by_index(1)

print(mark)

mark.remove_card_by_suit_rank('H', '4')
mark.remove_card_by_suit_rank('S', '6')
print(f'Mark has {len(mark)} cards:  {mark}')

exit()



from deck import Deck

d = Deck()
# print(f'{len(d)} cards:  {d}')

d.shuffle()
print(f'{len(d)} cards:  {d}')

d.deal_cards(40)
print(f'{len(d)} cards:  {d}')

exit()



from card import Card

a = Card(suit='C', rank='6')
print(f'{a} has value of {a.value}')
print(a.get_full())

b = Card(suit='H', rank='K')
print(f'{b} has value of {b.value}')

if a.value > b.value:
    print(f'{a} > {b}')
elif a.value < b.value:
    print(f'{a} < {b}')
else:
    print(f'{a} == {b}')

