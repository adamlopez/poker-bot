from objects import Card, Player, HandValue as HandVal
import itertools
import time
from random import shuffle
from collections import deque
from typing import List, Dict
SUITS = ['H','D','S','C']

CARDS = [i for i in range(2,15)]




class Session:
    ALL_CARDS = []
    for i in range(1,14):
        for suit in SUITS:
            ALL_CARDS.append(Card(suit,i))
    POSSIBLE_TABLES = list(itertools.combinations(ALL_CARDS,5))

    def __init__(self,log,playerCount=2):
        self.log = log
        self.log.info('New session started.')
        self.COMMUNITY_CARDS = []
        self.deck = deque(self.ALL_CARDS)
        self.players = []
        for i in range(playerCount):
            self.players.append(Player(position=i))
            print(self.players)

    def getGameOutcome(self):
        outcomes = []

    def showState(self) -> None:
        for player in self.players:
            self.log.info(f"{player.name}'s hand: {player.hand}")
        self.log.info(f"Community Cards: {self.COMMUNITY_CARDS}")


    def newGame(self):
        '''starts a new game by resetting all Session attributes as needed.'''
        self.COMMUNITY_CARDS = []
        self.log.info('shuffling...')
        shuffle(self.deck)
        #assign cards to players hands
        for player in self.players:
            player.hand = []
            player.hand.append(self.deck.pop())
            player.hand.append(self.deck.pop())
        for i in range(5):
            self.COMMUNITY_CARDS.append(self.deck.pop())

    def _getHighCards(self, player_num: int, num_cards) -> List[Card]:
        """returns a list of the <num_cards> highest cards between player
        <player_num> and the community cards.
        """
        ls = self.players[player_num].hand + self.COMMUNITY_CARDS,
        sortedCards = sorted(ls, key=lambda card: card.value)
        idx = num_cards * -1
        kickers[HandVal.HIGH_CARD] = sortedCards[idx:][::-1]

    def getBestHands(self):
        ''' returns a string representation of the best hands
            each player holds.'''
        results = {}
        for player in self.players:
            empties = [[None for i in range(5)] for k in range(len(HandVal))]
            kickers = dict(zip(HandVal, empties))
            cards = player.hand + self.COMMUNITY_CARDS

            zeros = [0 for i in range(len(HandVal))]
            handcounts = dict(zip(HandVal, zeros))
            suitcounts = dict(zip(SUITS,[0 for i in range(len(SUITS))]))

            #high card
            sortedCards = sorted(player.hand + self.COMMUNITY_CARDS,
                                key=lambda card: card.value)
            handcounts[HandVal.HIGH_CARD] = sortedCards[-1].value
            kickers[HandVal.HIGH_CARD] = sortedCards[-5:][::-1]

            # check for pair, trips and quads
            counted = []
            for baseCard in cards:
                suitcounts[baseCard.suit] += 1
                valCount = 1
                #create copy of list with base card removed
                withoutBase = [x for x in cards if x != baseCard]
                for card in withoutBase:
                    if baseCard.value == card.value and baseCard not in counted:
                        valCount += 1
                        counted.append(card)

                if valCount == 2:
                    kickers[HandVal.PAIR][handcounts[HandVal.PAIR]] = baseCard.value
                    handcounts[HandVal.PAIR] += 1
                    self.log.info(f"pair! ({player})")
                elif valCount == 3:
                    kickers[HandVal.TRIPS][handcounts[HandVal.TRIPS]] = baseCard.value
                    handcounts[HandVal.TRIPS] += 1
                    self.log.info(f'trips! ({player})')
                elif valCount == 4:
                    kickers[HandVal.QUADS][0:4] = baseCard.value
                    handcounts[HandVal.QUADS] += 1
                    kickers[-1] = baseCard.value
                    self.log.info(f'quads! ({player})')

            if handcounts[HandVal.PAIR] > 1:
                handcounts[HandVal.TWO_PAIR] += 1
                kickers[HandVal.TWO_PAIR] = kickers[HandVal.TWO_PAIR]
                self.log.info(f'two pair! ({player})')

            if handcounts[HandVal.PAIR] >= 1 and handcounts[HandVal.TRIPS] >= 1:
                handcounts[HandVal.FULL_HOUSE] += 1
                kickers[HandVal.FULL_HOUSE][0] = kickers[HandVal.TRIPS][0]
                kickers[HandVal.FULL_HOUSE][1] = kickers[HandVal.PAIR][0]
                self.log.info(f'full house! ({player})')

            for v in suitcounts.values():
                if v >= 5:
                    handcounts[HandVal.FLUSH] += 1
                    self.log.info(f'flush! ({player})')
            sortedCards = sorted(cards,key=lambda card: card.value)
            self.log.debug(f'sorted cards: {sortedCards}')
            if sortedCards[-1].value == 14: #count ace as lowest and highest
                sortedCards.insert(0,Card(sortedCards[-1].suit,1))
                self.log.debug(f'sorted cards post insert: {sortedCards}')
            prevNum = -1
            suitStreak = 0
            streak = 1
            prevSuit = [sortedCards[0].suit]
            for card in sortedCards:
                self.log.debug(f'\ncard: {card}')
                if prevNum + 1 == card.value:
                    streak += 1
                    for suit in prevSuit:
                        if suit == card.suit:
                            suitStreak = suitStreak + 1
                            prevSuit = [suit]
                            break
                        suitStreak = 1
                elif prevNum == card.value:
                    streak = streak
                    suitStreak = suitStreak
                    prevSuit.append(card.suit)
                else:
                    streak = 1
                    suitStreak = 1
                    prevSuit = [card.suit]

                #append high cards to fill the kickers array


                self.log.debug(f'value streak: {streak}')
                self.log.debug(f'suit streak: {suitStreak}')
                prevNum = card.value
                self.log.debug(f'prev suit: {prevSuit}')
                if streak >= 5 and  suitStreak >= 5:
                    if card.value == 14:
                        self.log.info(f'{card.suit} royal flush! ({player})')
                        handcounts[HandVal.ROYAL_FLUSH] = 1
                    else:
                        self.log.info(f'{card}-high straight flush! ({player})')
                    handcounts[HandVal.STRAIGHT_FLUSH] = 1
                elif streak >= 5:
                    self.log.debug(f'{card}-high straight! ({player})')
                    handcounts[HandVal.STRAIGHT] = 1


            for hand,freq in handcounts.items():
                self.log.debug(f"{hand}:{freq}")
                if freq > 0: #will automatically take the highest ranked hand
                    results[player] = (hand,kickers[hand])
                    break

        return results
