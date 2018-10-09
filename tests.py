import time
start = time.perf_counter()
from objects import Card, Player
from session import Session
from logger import getLogger
import sys
import pytest
logger = getLogger()

def test_high_card():
    sesh = Session(logger,playerCount=2)
    players = ['Adam','Verina']
    for i in range(len(players)):
        sesh.players[i].name = players[i]
    sesh.newGame()
    sesh.players[0].hand[0] = Card('H',12)
    sesh.players[0].hand[1] = Card('S',14)

    sesh.players[1].hand[0] = Card('C',2)
    sesh.players[1].hand[1] = Card('D',6)

    sesh.COMMUNITY_CARDS[0] = Card('D',10)
    sesh.COMMUNITY_CARDS[1] = Card('S',9)
    sesh.COMMUNITY_CARDS[2] = Card('C',5)
    sesh.COMMUNITY_CARDS[3] = Card('D',3)
    sesh.COMMUNITY_CARDS[4] = Card('C',13)
    sesh.showState()
    res = sesh.getBestHands()
    assert res[sesh.players[0]][0] == 'high card'
    assert res[sesh.players[0]][1] == [14, 13, 12, 10, 9]
    assert res[sesh.players[1]][0] == 'high card'
    assert res[sesh.players[1]][1] == [13, 10, 9, 6, 5]



def test_full_house_pair():
    sesh = Session(logger,playerCount=2)
    players = ['Adam','Verina']
    for i in range(len(players)):
        sesh.players[i].name = players[i]
    sesh.newGame()
    sesh.players[0].hand[0] = Card('H',12)
    sesh.players[0].hand[1] = Card('S',12)

    sesh.players[1].hand[0] = Card('C',10)
    sesh.players[1].hand[1] = Card('D',8)

    sesh.COMMUNITY_CARDS[0] = Card('D',10)
    sesh.COMMUNITY_CARDS[1] = Card('S',10)
    sesh.COMMUNITY_CARDS[2] = Card('C',8)
    sesh.COMMUNITY_CARDS[3] = Card('D',7)
    sesh.COMMUNITY_CARDS[4] = Card('C',12)
    sesh.showState()
    res = sesh.getBestHands()
    assert res[sesh.players[0]][0] == 'full house'
    assert res[sesh.players[1]][0] == 'full house'

def test_pockets():
    sesh = Session(logger,playerCount=2)
    players = ['Adam','Verina']
    for i in range(len(players)):
        sesh.players[i].name = players[i]
    sesh.newGame()
    sesh.players[0].hand[0] = Card('H',12)
    sesh.players[0].hand[1] = Card('S',12)
    sesh.players[1].hand[0] = Card('C',10)
    sesh.players[1].hand[1] = Card('S',10)
    sesh.COMMUNITY_CARDS[0] = Card('H',9)
    sesh.COMMUNITY_CARDS[1] = Card('S',4)
    sesh.COMMUNITY_CARDS[2] = Card('C',8)
    sesh.COMMUNITY_CARDS[3] = Card('D',7)
    sesh.COMMUNITY_CARDS[4] = Card('C',13)
    res = sesh.getBestHands()
    assert res[sesh.players[0]][0] == 'pair'
    assert res[sesh.players[1]][0] == 'pair'

def test_flush_1():
    sesh = Session(logger,playerCount=2)
    players = ['Adam','Verina']
    for i in range(len(players)):
        sesh.players[i].name = players[i]
    sesh.newGame()
    sesh.players[0].hand[0] = Card('H',12)
    sesh.players[0].hand[1] = Card('S',13)
    sesh.players[1].hand[0] = Card('D',10)
    sesh.players[1].hand[1] = Card('D',8)

    sesh.COMMUNITY_CARDS[0] = Card('H',10)
    sesh.COMMUNITY_CARDS[1] = Card('C',10)
    sesh.COMMUNITY_CARDS[2] = Card('D',5)
    sesh.COMMUNITY_CARDS[3] = Card('D',7)
    sesh.COMMUNITY_CARDS[4] = Card('D',12)
    res = sesh.getBestHands()
    assert res[sesh.players[0]][0] == 'two pair'
    assert res[sesh.players[1]][0] == 'flush'

def test_straight_1():
    sesh = Session(logger,playerCount=2)
    players = ['Adam','Verina']
    for i in range(len(players)):
        sesh.players[i].name = players[i]
    sesh.newGame()
    sesh.players[0].hand[0] = Card('S',12)
    sesh.players[0].hand[1] = Card('C',11)
    sesh.players[1].hand[0] = Card('D',10)
    sesh.players[1].hand[1] = Card('D',8)
    sesh.COMMUNITY_CARDS[0] = Card('S',10)
    sesh.COMMUNITY_CARDS[1] = Card('D',9)
    sesh.COMMUNITY_CARDS[2] = Card('C',8)
    sesh.COMMUNITY_CARDS[3] = Card('D',7)
    sesh.COMMUNITY_CARDS[4] = Card('C',12)
    res = sesh.getBestHands()
    assert res[sesh.players[0]][0] == 'straight'
    assert res[sesh.players[1]][0] == 'two pair'

def test_ace_high_straight():
    sesh = Session(logger,playerCount=2)
    players = ['Adam','Verina']
    for i in range(len(players)):
        sesh.players[i].name = players[i]
    sesh.newGame()
    sesh.players[0].hand[0] = Card('S',14)
    sesh.players[0].hand[1] = Card('C',2)
    sesh.players[1].hand[0] = Card('D',10)
    sesh.players[1].hand[1] = Card('D',8)
    sesh.COMMUNITY_CARDS[0] = Card('S',13)
    sesh.COMMUNITY_CARDS[1] = Card('D',12)
    sesh.COMMUNITY_CARDS[2] = Card('C',11)
    sesh.COMMUNITY_CARDS[3] = Card('D',7)
    sesh.COMMUNITY_CARDS[4] = Card('C',10)
    res = sesh.getBestHands()
    assert res[sesh.players[0]][0] == 'straight'
    assert res[sesh.players[1]][0] == 'pair'

def test_ace_low_straight():
    sesh = Session(logger,playerCount=2)
    players = ['Adam','Verina']
    for i in range(len(players)):
        sesh.players[i].name = players[i]
    sesh.newGame()
    sesh.players[0].hand[0] = Card('S',14)
    sesh.players[0].hand[1] = Card('C',2)
    sesh.players[1].hand[0] = Card('D',10)
    sesh.players[1].hand[1] = Card('D',8)
    sesh.COMMUNITY_CARDS[0] = Card('S',3)
    sesh.COMMUNITY_CARDS[1] = Card('D',4)
    sesh.COMMUNITY_CARDS[2] = Card('C',5)
    sesh.COMMUNITY_CARDS[3] = Card('D',9)
    sesh.COMMUNITY_CARDS[4] = Card('C',10)
    res = sesh.getBestHands()
    assert res[sesh.players[0]][0] == 'straight'
    assert res[sesh.players[1]][0] == 'pair'

def test_straight_flush_1():
    sesh = Session(logger,playerCount=2)
    players = ['Adam','Verina']
    for i in range(len(players)):
        sesh.players[i].name = players[i]
    sesh.newGame()
    sesh.players[0].hand[0] = Card('S',14)
    sesh.players[0].hand[1] = Card('S',2)
    sesh.players[1].hand[0] = Card('D',10)
    sesh.players[1].hand[1] = Card('D',8)
    sesh.COMMUNITY_CARDS[0] = Card('S',3)
    sesh.COMMUNITY_CARDS[1] = Card('S',4)
    sesh.COMMUNITY_CARDS[2] = Card('S',5)
    sesh.COMMUNITY_CARDS[3] = Card('D',6)
    sesh.COMMUNITY_CARDS[4] = Card('C',10)
    res = sesh.getBestHands()
    assert res[sesh.players[0]][0] == 'straight flush'
    assert res[sesh.players[1]][0] == 'pair'

def test_straight_flush_2():
    sesh = Session(logger,playerCount=2)
    players = ['Adam','Verina']
    for i in range(len(players)):
        sesh.players[i].name = players[i]
    sesh.newGame()
    sesh.players[0].hand[0] = Card('D',10)
    sesh.players[0].hand[1] = Card('D',8)
    sesh.players[1].hand[0] = Card('C',6)
    sesh.players[1].hand[1] = Card('C',2)
    sesh.COMMUNITY_CARDS[0] = Card('C',3)
    sesh.COMMUNITY_CARDS[1] = Card('C',4)
    sesh.COMMUNITY_CARDS[2] = Card('C',5)
    sesh.COMMUNITY_CARDS[3] = Card('D',7)
    sesh.COMMUNITY_CARDS[4] = Card('C',10)
    res = sesh.getBestHands()
    assert res[sesh.players[0]][0] == 'pair'
    assert res[sesh.players[1]][0] == 'straight flush'

def test_royal_flush_1():
    sesh = Session(logger,playerCount=2)
    players = ['Adam','Verina']
    for i in range(len(players)):
        sesh.players[i].name = players[i]
    sesh.newGame()
    sesh.players[0].hand[0] = Card('D',10)
    sesh.players[0].hand[1] = Card('D',12)
    sesh.players[1].hand[0] = Card('C',6)
    sesh.players[1].hand[1] = Card('C',2)

    sesh.COMMUNITY_CARDS[0] = Card('D',14)
    sesh.COMMUNITY_CARDS[1] = Card('D',11)
    sesh.COMMUNITY_CARDS[2] = Card('D',2)
    sesh.COMMUNITY_CARDS[3] = Card('D',7)
    sesh.COMMUNITY_CARDS[4] = Card('D',13)
    res = sesh.getBestHands()
    assert res[sesh.players[0]][0] == 'royal flush'
    assert res[sesh.players[1]][0] == 'flush'

def test_royal_flush_2():
    sesh = Session(logger,playerCount=2)
    players = ['Adam','Verina']
    for i in range(len(players)):
        sesh.players[i].name = players[i]
    sesh.newGame()
    sesh.players[0].hand[0] = Card('D',10)
    sesh.players[0].hand[1] = Card('D',12)
    sesh.players[1].hand[0] = Card('C',8)
    sesh.players[1].hand[1] = Card('C',2)
    sesh.COMMUNITY_CARDS[0] = Card('D',14)
    sesh.COMMUNITY_CARDS[1] = Card('D',11)
    sesh.COMMUNITY_CARDS[2] = Card('C',10)
    sesh.COMMUNITY_CARDS[3] = Card('D',7)
    sesh.COMMUNITY_CARDS[4] = Card('D',13)
    res = sesh.getBestHands()
    assert res[sesh.players[0]][0] == 'royal flush'
    assert res[sesh.players[1]][0] == 'high card'

if __name__ == '__main__':
    import pytest
    pytest.main(['tests.py'])
