import time
start = time.clock()
import datetime
import random

class Card:
    def __init__(self,suit,value,visible=False):
        self.value = value
        self.suit = suit
        self.visible = visible

    def __repr__(self):
        return self.suit + str(self.value)

    def __eq__(self,other):
        if isinstance(other,Card):
            if (other.suit == self.suit) and (other.value == self.value):
                return True
            return False #if suit & value aren't equal
        return False #if not a Card object

class Player:
    STARTING_CHIPS = 100

    def __init__(self,pos=0,hand=[],chips=STARTING_CHIPS):
        self.pos = pos
        self.hand = hand
        self.chips = chips
