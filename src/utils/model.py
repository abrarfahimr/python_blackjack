import random

# Setup global variables

# Suits
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

# Ranks
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

# Values
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}

# Initialize boolean for while loop
playing = True


# CLASS DEFINITION

# Card Class
class Card:
    def __init__(self, suit, rank) -> None:
        self.suit = suit
        self.rank = rank

    # if asked to print a card, returns the string in the form of its rank and suit eg. "Two of Hearts"
    def __str__(self) -> str:
        return self.rank + ' of ' + self.suit


# Deck Class
class Deck:
    def __init__(self) -> None:
        self.deck = []
        for suit in suits:
            for rank in ranks:
                # build a list of all variation of cards
                self.deck.append(Card(suit, rank))

    def __str__(self) -> str:
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()  # add each Card object's print string
        return 'The deck has: ' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)  # Shuffle the deck for every game

    def deal(self):
        # pick the last card from the deck. We are considering the top card to be the last
        single_card = self.deck.pop()
        return single_card


# Hand Class
class Hand:
    def __init__(self) -> None:
        self.cards = []  # start with empty hand with no cards
        self.value = 0  # start with a 0 valur
        self.aces = 0  # start with not aces

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1  # add to self.aces

    def adjust_for_ace(self):
        # if the value is over 21 and they have an ace we subtract 10 from value to stay under 21
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


# Chip Class
class Chip:
    def __init__(self) -> None:
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet  # Increase the total if player wins

    def lose_bet(self):
        self.total -= self.bet  # Decrease the total if player lose
