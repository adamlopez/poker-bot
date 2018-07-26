from person import Card, Player
import itertools
import time
from random import shuffle
from collections import deque
class Session:
    SUITS = ['H','D','S','C']
    CARDS = [i for i in range(2,15)]
    ALL_CARDS = []
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

    for i in range(1,14):
        for suit in SUITS:
            ALL_CARDS.append(Card(suit,i))
    POSSIBLE_TABLES = list(itertools.combinations(ALL_CARDS,5))

    def __init__(self,logger,players=2):
        self.logger = logger
        self.logger.info('New session started.')
        self.COMMUNITY_CARDS = []
        self.deck = deque(self.ALL_CARDS)
        self.players = [Player() for i in range(players)]

    def getGameOutcome(self):
        outcomes = []

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
            self.logger.info(f"Player {player.pos}'s hand: {player.hand}")
        for i in range(5):
            self.COMMUNITY_CARDS.append(self.deck.pop())
        self.logger.info(f"Community Cards: {self.COMMUNITY_CARDS}")


    def getBestHands(self):
        ''' returns a string representation of the best hands each player holds.'''
        for player in self.players:
            cards = player.hand + self.COMMUNITY_CARDS
            print(cards)

            handcounts = dict(zip(self.HAND_RANKS.keys(),[0 for i in range(len(self.HAND_RANKS.keys()))]))
            suitcounts = dict(zip(self.SUITS,[0 for i in range(len(self.SUITS))]))

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
                        print(baseCard,card)
                        valCount += 1
                        counted.append(card)

                if valCount == 2:
                    handcounts['pair'] += 1
                    print("pair!")
                elif valCount == 3:
                    handcounts['trips'] += 1
                    print('trips!')
                elif valCount == 4:
                    handcounts['quads'] += 1
                    print('quads!!')

            if handcounts['pair'] >= 1:
                handcounts['two pair'] += 1

            if handcounts['pair'] >= 1 and handcounts['trips'] >= 1:
                handcounts['full house'] += 1
                print('full house!')

            for v in suitcounts.values():
                if v >= 5:
                    handcounts['flush'] += 1
                    print('flush!')
            prevNum = -1
            streak = 1
            print(sortedCards)
            if sortedCards[-1] == 14: #count ace as lowest and highest
                sortedCards.insert(0,1)
                print('INSERTING')
            print(sortedCards)
            for num in sortedCards:
                print(f'card: {num}')
                if prevNum+1 == num:
                    streak+=1
                elif prevNum == num:
                    streak = streak
                else:
                    streak = 1
                print(f'streak: {streak}')
                prevNum = num
                if streak >= 5:
                    print('straight!')
                    handcounts['straight'] = 1
            print(handcounts)
