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
        while self.value > 21 and self.aces > 0:
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


# Ask how many chips player wants to bet
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except ValueError:
            print('Sorry, a bet must be an integer')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed", chips.total)
            else:
                break

# Taking a hit until bust


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

# ask if the player wants to hit or stand


def hit_or_stand(deck, hand):
    global playing  # to control the while loop

    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")

        if x[0].lower() == 'h':
            hit(deck, hand)

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break

# DISPLAY CARDS
# display cards, show one card for the dealer and both cards for player


def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')

# display cards, show both cards for player and dealer


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)


# END GAME SCENARIOS
# Player busts
def player_busts(player, dealer, chips):
    print("Player busts!")
    chips.lose_bet()

# Player wins


def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()

# Dealer busts


def dealer_busts(player, dealer, chips):
    print("Dealer busts!")
    chips.win_bet()

# Dealer wins


def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose_bet()

# if the value of cards are the same


def push(player, dealer):
    print("Dealer and Player tie! It's a push.")


while True:
    # Print an opening statement
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the Player's chips
    player_chips = Chip()  # remember the default value is 100

    # Prompt the Player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        # Show all cards
        show_all(player_hand, dealer_hand)

        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        else:
            push(player_hand, dealer_hand)

    # Inform Player of their chips total
    print("\nPlayer's winnings stand at", player_chips.total)

    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing!")
        break
