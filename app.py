"""Run the War game application."""

import time

import settings

import card
import deck
import player


def show_status(player1, player2):
    """Show current card status of each player."""
    if len(player1) == len(player2):
        print(f'Both players have {len(player1)} cards.')
    else:
        print(f'Player1 has {len(player1)} cards, and Player2 has {len(player2)} cards.')

def main():
    """Run application."""

    # Create player 1
    player_name = input('Enter name for player 1: ')
    player1 = player.Player(player_name)

    # Create player 2
    player_name = input('Enter name for player 2: ')
    player2 = player.Player(player_name)

    # Setup deck
    d = deck.Deck()
    d.shuffle()

    # Deal cards to each player until the deck is empty.
    for _ in range(int(len(d)/2)):
        # each round of dealing, give one card to each player
        player1.add_cards(d.deal_cards(1))
        player2.add_cards(d.deal_cards(1))

    # Show status.
    print('\nLet\'s play War!')
    show_status(player1, player2)

    # Ask for key press to start game.
    input('The game is ready to begin. Press <ENTER> to continue.')


    # Play the game by a series of rounds, with pause between.
    game_round = 0
    while len(player1) > 0 and len(player2) > 0:
        game_round += 1
        print(f'\n\nRound {game_round}')

        # Players play 1 card
        player1_cards = []
        player2_cards = []

        player1.play_cards_faceup(1)
        player2.play_cards_faceup(1)

        for _ in player1.table_face_up:
            print(_)
        print("  ")
        for _ in player2.table_face_up:
            print(_)

        exit()

        # Compare cards played
        if player1_cards[0].rank > player2_cards[0].rank:
            # Player1 wins
            print(f'{player1.name} (player 1) wins the round.')
            # Move Player1's card to the bottom of Player1's hand.
            player1.add_cards(player1.remove_card_by_index(-1))
            # Move Player2's card to the bottom of Player1's hand.
            player1.add_cards(player2.remove_card_by_index(-1))
        elif player2_cards[0].rank > player1_cards[0].rank:
            # Player2 wins
            print(f'{player2.name} (player 2) wins the round.')
            # Move Player2's card to the bottom of Player2's hand.
            player2.add_cards(player2.remove_card_by_index(-1))
            # Move Player2's card to the bottom of Player1's hand.
            player2.add_cards(player1.remove_card_by_index(-1))
        else:
            print('Tie')

            # For now, just return the cards
            player1.add_cards(player1.remove_card_by_index(-1))
            player2.add_cards(player2.remove_card_by_index(-1))

        time.sleep(3)

        # Players play a list of cards from 1+ cards
        # In case of tie, each player plays up to 3 cards then plays again

    # Game is over - see who won
    if len(player1) == 0:
        print("Player1 out of cards! Game Over")
        print(f"Player2 wins in {game_round} rounds!")

    if len(player2) == 0:
        print("Player2 out of cards! Game Over")
        print(f"Player1 wins in {game_round} rounds!")


if __name__ == "__main__":
    main()
