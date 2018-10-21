""" Holds the Session class of a poker game.
    the session is responsible for encapsulating the logic and rules of the game.
"""

import itertools
from random import shuffle
from collections import deque
from typing import List
from objects import Card, Player, HandValue as HandVal

SUITS = ['H', 'D', 'S', 'C']
CARDS = [i for i in range(2, 15)]


class Session:
    ALL_CARDS = []
    for i in range(1, 14):
        for suit in SUITS:
            ALL_CARDS.append(Card(suit, i))
    POSSIBLE_TABLES = list(itertools.combinations(ALL_CARDS, 5))

    def __init__(self, log, playerCount=2):
        self.log = log
        self.log.info('New session started.')
        self.community_cards = []
        self.deck = deque(self.ALL_CARDS)
        self.players = []
        for i in range(playerCount):
            self.players.append(Player(position=i))

    def get_game_outcome(self):
        pass

    def log_state(self) -> None:
        for player in self.players:
            self.log.info(f"{player.name}'s hand: {player.hand}")
        self.log.info(f"Community Cards: {self.community_cards}")


    def setup_game(self):
        """starts a new game by resetting all Session attributes as needed."""
        self.community_cards = []
        self.log.info('shuffling...')
        shuffle(self.deck)
        #assign cards to players hands
        for player in self.players:
            player.hand = []
            player.hand.append(self.deck.pop())
            player.hand.append(self.deck.pop())
        for _ in range(5):
            self.community_cards.append(self.deck.pop())

    def _get_high_cards(self, player_num: int, num_cards) -> List[Card]:
        """returns a list of the <num_cards> highest cards between player
        <player_num> and the community cards.
        """
        all_cards = self.players[player_num].hand + self.community_cards
        sorted_cards = sorted(all_cards, key=lambda card: card.value)
        idx = num_cards * -1
        return sorted_cards[idx:][::-1]

    def _compute_pair_frequencies(self, player, handcounts,
                                  suitcounts, kickers) -> None:
        """Computes the frequencies of pairs, trips, quads and full houses.
           Categorizes kickers based on hand-appropriate logic.
        """
        # check for pair, trips and quads
        counted = []
        cards = player.hand + self.community_cards
        for base_card in cards:
            suitcounts[base_card.suit] += 1
            val_count = 1
            #create copy of list with base card removed
            without_base = [x for x in cards if x != base_card]
            for card in without_base:
                if base_card.value == card.value and base_card not in counted:
                    val_count += 1
                    counted.append(card)

            if val_count == 2:
                kickers[HandVal.PAIR][handcounts[HandVal.PAIR]] = base_card.value
                handcounts[HandVal.PAIR] += 1
                self.log.info(f"pair! ({player})")
            elif val_count == 3:
                kickers[HandVal.TRIPS][handcounts[HandVal.TRIPS]] = base_card.value
                handcounts[HandVal.TRIPS] += 1
                self.log.info(f'trips! ({player})')
            elif val_count == 4:
                kickers[HandVal.QUADS][0:4] = base_card.value
                handcounts[HandVal.QUADS] += 1
                self.log.info(f'quads! ({player})')

        if handcounts[HandVal.PAIR] > 1:
            handcounts[HandVal.TWO_PAIR] += 1
            kickers[HandVal.TWO_PAIR] = sorted(
                kickers[HandVal.PAIR] + kickers[HandVal.PAIR])
            self.log.info(f'two pair! ({player})')

        if handcounts[HandVal.PAIR] >= 1 and handcounts[HandVal.TRIPS] >= 1:
            handcounts[HandVal.FULL_HOUSE] += 1
            kickers[HandVal.FULL_HOUSE][0] = kickers[HandVal.TRIPS][0]
            kickers[HandVal.FULL_HOUSE][1] = kickers[HandVal.PAIR][0]
            self.log.info(f'full house! ({player})')

    # FIXME: needs to be broken up
    def get_best_hands(self):
        """returns a string representation of the best hands
            each player holds. with the kcikers sorted from highest  to lowest.
        """
        results = {}
        for player in self.players:
            empties = [[0 for i in range(5)] for k in enumerate(HandVal)]
            kickers = dict(zip(HandVal, empties))
            cards = player.hand + self.community_cards
            handcounts = dict(zip(HandVal, [0 for i in enumerate(HandVal)]))
            suitcounts = dict(zip(SUITS, [0 for i in enumerate(SUITS)]))

            #high card
            sorted_cards = sorted(player.hand + self.community_cards,
                                  key=lambda card: card.value)
            handcounts[HandVal.HIGH_CARD] = sorted_cards[-1].value
            kickers[HandVal.HIGH_CARD] = sorted_cards[-5:][::-1]
            self._compute_pair_frequencies(player, handcounts, suitcounts, kickers)
            sorted_cards = sorted(cards, key=lambda card: card.value)
            self.log.debug(f'sorted cards: {sorted_cards}')
            for suit, freq in suitcounts.items():
                if freq >= 5:
                    handcounts[HandVal.FLUSH] += 1
                    self.log.info(f'flush! ({player})')
                    inc = 0
                    self.log.debug(sorted_cards[::-1])
                    for card_ in sorted_cards[::-1]:
                        if card_.suit == suit:
                            kickers[HandVal.FLUSH][inc] = card_.value
                            inc += 1
                        if inc == 5:
                            break
            if sorted_cards[-1].value == 14: #count ace as lowest and highest
                sorted_cards.insert(0, Card(sorted_cards[-1].suit, 1))
                self.log.debug(f'sorted cards post insert: {sorted_cards}')
            # TODO:make this standalone helper method
            prev_num = -1
            suit_streak = 0
            streak = 1
            prev_suit = [sorted_cards[0].suit]
            for card in sorted_cards:
                self.log.debug(f'\ncard: {card}')
                if prev_num + 1 == card.value:
                    streak += 1
                    for suit in prev_suit:
                        if suit == card.suit:
                            suit_streak = suit_streak + 1
                            prev_suit = [suit]
                            break
                        suit_streak = 1
                elif prev_num == card.value:
                    streak = streak
                    suit_streak = suit_streak
                    prev_suit.append(card.suit)
                else:
                    streak = 1
                    suit_streak = 1
                    prev_suit = [card.suit]

                #append high cards to fill the kickers array
                self.log.debug(f'value streak: {streak}')
                self.log.debug(f'suit streak: {suit_streak}')
                self.log.debug(f'prev suit: {prev_suit}')
                prev_num = card.value
                if streak >= 5 and suit_streak >= 5:
                    if card.value == 14:
                        self.log.info(f'{card.suit} royal flush! ({player})')
                        range_ = reversed(range(card.value-4, card.value+1))
                        kickers[HandVal.ROYAL_FLUSH] = [i for i in range_]
                        handcounts[HandVal.ROYAL_FLUSH] = 1
                    else:
                        self.log.info(f'{card}-high straight flush! ({player})')
                    range_ = reversed(range(card.value-4, card.value+1))
                    kickers[HandVal.STRAIGHT_FLUSH] = [i for i in range_]
                    handcounts[HandVal.STRAIGHT_FLUSH] = 1
                elif streak >= 5:
                    self.log.debug(f'{card}-high straight! ({player})')
                    handcounts[HandVal.STRAIGHT] = 1
                    range_ = reversed(range(card.value-4, card.value+1))
                    kickers[HandVal.STRAIGHT] = [i for i in range_]


            for hand, freq in handcounts.items():
                self.log.debug(f"{hand}:{freq}")
                if freq > 0: #will automatically take the highest ranked hand
                    results[player] = (hand, kickers[hand])
                    break

        return results
