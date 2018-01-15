import random
import math
from collections import deque
import itertools
import sys


def play_war_trick(d1, d2):
    # Take cards from the left of the deck, and put winnings on the right. In-place.

    p1_placed = [d1.popleft()]
    p2_placed = [d2.popleft()]

    winner = None
    if p1_placed[-1] > p2_placed[-1]:
        winner = 1
    elif p1_placed[-1] < p2_placed[-1]:
        winner = 2

    while not winner:
        # Currently there's a tie. Try to break it.

        if len(d1) == 0:
            # P1 ran out of cards entirely, so they're out of luck
            winner = 2
        elif len(d2) == 0:
            # P2 ran out of cards entirely, so they're out of luck
            winner = 1
        else:
            # Everyone's got some cards. Put 'em down
            p1_placed.append(d1.popleft())
            p2_placed.append(d2.popleft())

            # If a player only had 1 card at the time of the tie, it's okay for them to only put that down.
            # If they have another, though, that's the one that will count for breaking the tie.
            if len(d1) > 0:
                p1_placed.append(d1.popleft())
            if len(d2) > 0:
                p2_placed.append(d2.popleft())

            # Does anyone win now?
            if p1_placed[-1] > p2_placed[-1]:
                winner = 1
            elif p1_placed[-1] < p2_placed[-1]:
                winner = 2

    # The winner takes the cards in the order they're on the table, their own first
    if winner == 1:
        d1.extend(p1_placed)
        d1.extend(p2_placed)
    elif winner == 2:
        d2.extend(p2_placed)
        d2.extend(p1_placed)


def play_war(p1_deck_in, p2_deck_in):
    # Returns number (1 or 2) indicating the winner and a list of counts of cards in the winner's deck.
    # Copy data from the decks to prevent the outer scope's objects from being changed
    # (and get that sweet, sweet deque interface)
    num_cards = len(p1_deck_in) + len(p2_deck_in)
    p1_deck = deque(p1_deck_in, num_cards)
    p2_deck = deque(p2_deck_in, num_cards)

    p1_counts = [len(p1_deck)]

    for iter_num in itertools.count(1):
        play_war_trick(p1_deck, p2_deck)
        #print('After iter', iter_num, ': p1', len(p1_deck), 'p2', len(p2_deck))
        p1_counts.append(len(p1_deck))
        if len(p1_deck) == 0:
            # P2 won
            winner_counts = [num_cards - c for c in p1_counts]
            return 2, winner_counts
        if len(p2_deck) == 0:
            # P1 won
            winner_counts = p1_counts
            return 1, winner_counts


def run_fair_game(num_ranks, num_suits):
    # Deck is shuffled and split evenly between players
    deck = list(range(1, num_ranks + 1)) * num_suits

    random.shuffle(deck)
    half_deck = math.ceil(len(deck)/2)
    p1_deck = deck[:half_deck]
    p2_deck = deck[half_deck:]
    winner, winner_counts = play_war(p1_deck, p2_deck)
    return winner, winner_counts


def run_comeback_game(num_ranks, num_suits):
    # P2 starts with 1 card of highest rank, P1 with rest of the deck shuffled
    deck = list(range(1, num_ranks + 1)) * num_suits

    p2_deck = [deck.pop()]
    random.shuffle(deck)
    p1_deck = deck

    winner, winner_counts = play_war(p1_deck, p2_deck)
    return winner, winner_counts


def main(argv):
    if len(argv) >= 2:
        mode = argv[1]
    else:
        mode = 'fair'

    # Classic deck
    num_ranks = 13
    num_suits = 4

    if mode == 'fair':
        winner, winner_counts = run_fair_game(num_ranks=num_ranks, num_suits=num_suits)
    elif mode == 'comeback':
        winner, winner_counts = run_fair_game(num_ranks=num_ranks, num_suits=num_suits)
    else:
        print('Unknown mode', mode)
        return

    print('iter #\twinner\'s count')
    for iter_num, c in enumerate(winner_counts):
        print(iter_num, '\t', c)


if __name__ == '__main__':
    main(sys.argv)
