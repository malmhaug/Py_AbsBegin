# File: war.py
# Version: 1.0.0
# About: War game. The one who have the highest card value wins
# Date: 13 March 2016 | Jim-Kristian Malmhaug

from Deck import Card_deck
from player import Player
import sys

def main():
    player_list = []
    value_list = []
    sorted_list = []
    winner_list = []

    print("\nWelcome to the war game\nThe one who pick the highest card wins!\n")

    war = Card_deck()
    war.make_cards()
    war.shuffle_cards()
    try:
        players = int(input("How many players? (1-10)\n---> "))
        if players > 10:
            print("Not possible to have that much players.\nGame ends!")
            sys.exit()
    except ValueError as e:
        print("Something went wrong. Error: ", e)
        sys.exit()

    # Add card to person
    for person in range(players):
        player_list.append((Player().get_name(person), war.pick_card()))

    # Print and check card value
    print('\n')
    for player, the_card in player_list:
        print(player + ' has card: ' + the_card)
        value_list.append((player, war.check_value(the_card)))

    # Find person with highest card
    for player, card_value in value_list:
        sorted_list.append(card_value)
    sorted_list.sort(reverse=True)
    high_value = max(sorted_list)
    for player, card_value in value_list:
        if card_value == high_value:
            winner_list.append((player, card_value))
        else:
            pass

    # Check for draw or single win
    if len(winner_list) > 1:
        print("\nDraw between: ")
        for player, card_value in winner_list:
            print(player)
    else:
        print("\nWinner is: ", winner_list)

main()
input("\nPress enter to quit...")
