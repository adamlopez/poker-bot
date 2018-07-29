from person import Card, Player
import itertools
import time
from random import shuffle
from collections import deque

SUITS = ['H','D','S','C']
CARDS = [i for i in range(2,15)]
HAND_RANKS = {'royal flush' : 1,
              'straight flush' : 2,
              'quads' : 3,
              'full house':4,
              'flush':5,
              'straight':6,
              'trips':7,
              'two pair':8,
              'pair':9,
              'high card':10}

[i for i in HAND_RANKS.keys()]

class Session:
    ALL_CARDS = []

    for i in range(1,14):
        for suit in SUITS:
            ALL_CARDS.append(Card(suit,i))
    POSSIBLE_TABLES = list(itertools.combinations(ALL_CARDS,5))

    def __init__(self,logger,playerCount=2):
        self.logger = logger
        self.logger.info('New session started.')
        self.COMMUNITY_CARDS = []
        self.deck = deque(self.ALL_CARDS)
        self.players = []
        for i in range(playerCount):
            self.players.append(Player(position=i))
            print(self.players)

    def getGameOutcome(self):
        outcomes = []

    def showState(self):
        for player in self.players:
            self.logger.info(f"Player {player.position}'s hand: {player.hand}")
        self.logger.info(f"Community Cards: {self.COMMUNITY_CARDS}")


    def newGame(self):
        '''starts a new game by resetting all Session attributes as needed.'''
        self.COMMUNITY_CARDS = []
        self.logger.info('shuffling...')
        shuffle(self.deck)
        #assign cards to players hands
        for player in self.players:
            player.hand = []
            player.hand.append(self.deck.pop())
            player.hand.append(self.deck.pop())
        for i in range(5):
            self.COMMUNITY_CARDS.append(self.deck.pop())


    def getBestHands(self):
        ''' returns a string representation of the best hands each player holds.'''
        handValues = {'value streak','suit streak',''}
        for player in self.players:
            cards = player.hand + self.COMMUNITY_CARDS

            handcounts = dict(zip(HAND_RANKS.keys(),[0 for i in range(len(HAND_RANKS.keys()))]))
            suitcounts = dict(zip(SUITS,[0 for i in range(len(SUITS))]))

            #high card
            sortedCards = [card.value for card in player.hand]
            sortedCards.sort()
            handcounts['high card'] = sortedCards[-1]

            # check for pair, trips and quads
            counted = []
            for baseCard in cards:
                suitcounts[baseCard.suit] += 1
                valCount = 1
                withoutBase = [x for x in cards if x != baseCard] #return copy without the base card
                for card in withoutBase:
                    if baseCard.value == card.value and baseCard not in counted:
                        valCount += 1
                        counted.append(card)

                if valCount == 2:
                    handcounts['pair'] += 1
                    self.logger.info("pair!")
                elif valCount == 3:
                    handcounts['trips'] += 1
                    self.logger.info('trips!')
                elif valCount == 4:
                    handcounts['quads'] += 1
                    self.logger.info('quads!!')

            if handcounts['pair'] >= 1:
                handcounts['two pair'] += 1

            if handcounts['pair'] >= 1 and handcounts['trips'] >= 1:
                handcounts['full house'] += 1
                self.logger.info('full house!')

            for v in suitcounts.values():
                if v >= 5:
                    handcounts['flush'] += 1
                    self.logger.info(f'flush!')
            sortedCards = sorted(cards,key=lambda card: card.value)
            self.logger.debug(f'sorted deck: {sortedCards}')
            if sortedCards[-1].value == 14: #count ace as lowest and highest
                sortedCards.insert(0,Card(sortedCards[-1].suit,1))
                self.logger.debug(f'sorted cards post insert: {sortedCards}')
            prevNum = -1
            suitStreak = 0
            streak = 1
            prevSuit = [sortedCards[0].suit]
            for card in sortedCards:
                self.logger.debug(f'\ncard: {card}')
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

                self.logger.debug(f'value streak: {streak}')
                self.logger.debug(f'suit streak: {suitStreak}')
                prevNum = card.value
                print(f'prev suit: {prevSuit}')
                if streak >= 5 and  suitStreak >= 5:
                    self.logger.info(f'{card}-high straight flush!')
                    if card.value == 14:
                        self.logger.info(f'{card.suit} royal flush!!')
                        handcounts['royal flush'] = 1

                    handcounts['straight flush'] = 1
                elif streak >= 5:
                    self.logger.debug(f'{card}-high straight!')
                    handcounts['straight'] = 1

            self.logger.info(handcounts)
        for k,v in handcounts.items():
            if v > 1:
                return k,v
        return handcounts
