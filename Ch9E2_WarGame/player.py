from Deck import Card_deck


class Player(Card_deck):
    def __int__(self):
        self.name = None
        self.card = None

    def __str__(self):
        rep = "Player name: {0}".format(self.name)
        return rep

    def get_name(self, number):
        self.name = input("Enter name {0}: ".format(number+1))
        return self.name

    def get_card(self):
        self.card = Card_deck.pick_card(self)
        return  self.card
