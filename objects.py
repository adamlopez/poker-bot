""" Holds various container objects for use in a poker game."""
from enum import Enum

class Card:
    """ class object that defines a card of a Poker game."""
    def __init__(self, suit, value, visible=False):
        self.value = value
        self.suit = suit
        self.visible = visible

    def __repr__(self):
        return str(self.value) + self.suit

    def __eq__(self, other):
        if isinstance(other, Card):
            if (other.suit == self.suit) and (other.value == self.value):
                return True
            return False #if suit & value aren't equal
        return False #if not a Card object

class Player:
    """ claass object that defines a player of a Poker game."""
    STARTING_CHIPS = 100
    def __repr__(self):
        return str(self.name)

    def __init__(self, name=None, position=0, hand=None, chips=STARTING_CHIPS):
        self.name = name
        self.position = position
        self.hand = hand
        if hand is None:
            self.hand = []
        self._chips = chips

    def add_chips(self, amount):
        """add chips to the given player's stack."""
        self._chips += amount

class HandValue(Enum):
    """
    HandValue defines the possible hands a player can have, and inherits from
    Enum to make the hands iterable.
    """
    ROYAL_FLUSH = 10
    STRAIGHT_FLUSH = 9
    QUADS = 8
    FULL_HOUSE = 7
    FLUSH = 6
    STRAIGHT = 5
    TRIPS = 4
    TWO_PAIR = 3
    PAIR = 2
    HIGH_CARD = 1
