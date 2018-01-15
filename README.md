# war-cards

Simulation of [everyone's favorite deterministic card game](https://en.wikipedia.org/wiki/War_(card_game)).

## Why did you do this?

This program is meant to help answer questions like, "How many turns should we expect a game of War to take? What if there were a different number of suits or ranks?" and "How often can a player starting with a single card win the game?"

## How to run

The script `War.py` can be called as follows:
```
python War.py [mode]
```
where `mode` is a parameter with the value of "fair" or "comeback". If omitted, "fair" is the default.

The program produces as standard output a table of the number of cards the eventual winner had at each turn of the game.

## Game modes
- `fair`: each player starts with half of the shuffled deck
- `comeback`: one player starts with a single card of the highest rank (13 by default), and the other player starts with all the rest of the cards, shuffled
