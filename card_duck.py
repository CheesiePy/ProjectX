
class Hand():
    pass


class Card():
    def __init__(self, value):
        number_card = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        action_cards = ['draw2', 'peek', 'switch']
        if value in number_card or action_cards:
            self.value = value
        else:
            raise ValueError('Invalid card value')

    def __str__(self):
        """
        Return a string representation of the card.
        """

        return str(self.value)


class Duck():
    deck_size = 56

    def __init__(self):
        self.deck = []
        self.discard = []
        self.create_deck()

    def create_deck(self):
        for i in range(10):
            for j in range(4):
                self.deck.append(Card(i))

        for i in range(0, 3):
            self.deck.append(Card('draw2'))
            self.deck.append(Card('peek'))
            self.deck.append(Card('switch'))

    def shuffle(self):
        pass

    def draw(self):
        pass

    def __str__(self):
        return str(self.deck)


def main():
    duck = Duck()
    print(duck)
main()