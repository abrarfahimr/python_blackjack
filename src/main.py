import utils.model as model
import utils.view as view

# GAME LOGIC

while True:
    # Print Opening Statement
    print("Welcome to BlackJack! Get as close to 21 as you can without going over!\nDealer hits until they reach 17.")

    # Create and Shuffle the deck, deal two cards to each player
    deck = model.Deck()
    deck.shuffle()

    player_hand = model.Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = model.Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the Player chips
    player_chips = model.Chip()  # Default is 100

    # Prompt the Player to bet
    view.take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    view.show_some(player_hand, dealer_hand)

    while model.playing:

        # Prompt for Player to Hit or Stand
        model.hit_or_stand(deck, player_hand)

        # Show cards (but keep one dealer card hidden)
        view.show_some(player_hand, dealer_hand)

        # if the player's hand exceed 21, run player_bust and break out of the loop
        if player_hand.value > 21:
            view.player_busts(player_hand, dealer_hand, player_chips)
            break

    if player_hand.value <= 21:

        while dealer_hand.value < player_hand.value:
            model.hit(deck, dealer_hand)

        # Show all cards
        view.show_all(player_hand, dealer_hand)

        # Run different winning scenarios
        if dealer_hand.value > 21:
            view.dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            view.dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            view.player_wins(player_hand, dealer_hand, player_chips)
        else:
            view.push(player_hand, dealer_hand)

    # Inform Player of their chip total
    print("\nPlayer's winning stand at", player_chips.total)

    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

    if new_game[0].lower() == 'y':
        view.playing = True
        continue
    else:
        print("Thanks for playing!")
        break
