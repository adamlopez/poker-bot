import time
start = time.clock()
import datetime
import random
from enum import Enum
class Card:
    def __init__(self,suit,value,visible=False):
        self.value = value
        self.suit = suit
        self.visible = visible

    def __repr__(self):
        return str(self.value) + self.suit

    def __eq__(self,other):
        if isinstance(other,Card):
            if (other.suit == self.suit) and (other.value == self.value):
                return True
            return False #if suit & value aren't equal
        return False #if not a Card object

class Player:
    STARTING_CHIPS = 100
    def __repr__(self):
        return str(self.name)


    def __init__(self,name=None,position=0,hand=[],chips=STARTING_CHIPS):
        self.name = name
        self.position = position
        self.hand = hand
        self.chips = chips

class HandValue(Enum):
    """
    The following defines the possible hands a player can have.
    """
    #keep these sorted by best to worst hand
    ROYAL_FLUSH = 1
    STRAIGHT_FLUSH = 2
    QUADS= 3
    FULL_HOUSE= 4
    FLUSH= 5
    STRAIGHT= 6
    TRIPS= 7
    TWO_PAIR= 8
    PAIR= 9
    HIGH_CARD= 10
