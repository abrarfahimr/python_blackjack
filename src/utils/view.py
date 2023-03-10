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