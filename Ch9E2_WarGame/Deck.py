import random

class Card_deck(object):
    def __init__(self):
        self.cards = []
        self.value = int(0)

    def __str__(self):
        pass

    def make_cards(self):
        special_cards = ['Hearts A', 'Hearts J', 'Hearts Q', 'Hearts K',
                         'Spades A', 'Spades J', 'Spades Q', 'Spades K',
                         'Diamonds A', 'Diamonds J', 'Diamonds Q', 'Diamonds K',
                         'Clubs A', 'Clubs J', 'Clubs Q', 'Clubs K']
        for i in range(9):
            self.cards.append('Hearts '+str(i+2))
            self.cards.append('Spades '+str(i+2))
            self.cards.append('Diamonds '+str(i+2))
            self.cards.append('Clubs '+str(i+2))
        for card in special_cards:
            self.cards.append(card)
        return self.cards

    def shuffle_cards(self):
        random.shuffle(self.cards)
        return self.cards

    def pick_card(self):
        picked_card = self.cards.pop(0)
        return picked_card

    def check_value(self, the_card):
        if 'Q' in the_card:
            self.value = 12
        elif 'J' in the_card:
            self.value = 11
        elif 'A' in the_card:
            self.value = 1
        elif 'K' in the_card:
            self.value = 13
        elif 'Hearts' in the_card:
            self.value = int(the_card[len('Hearts '):])
        elif 'Spades' in the_card:
            self.value = int(the_card[len('Spades '):])
        elif 'Clubs' in the_card:
            self.value = int(the_card[len('Clubs '):])
        elif 'Diamonds' in the_card:
            self.value = int(the_card[len('Diamonds '):])
        else:
            pass
        return self.value

if __name__ == '__main__':
    test = Card_deck()
    test.make_cards()
    print(test.shuffle_cards())
