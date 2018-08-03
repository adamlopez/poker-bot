import time
start = time.clock()
from person import Card,Player
from session import Session
from logger import getLogger
import sys
logger = getLogger()

def runTest(testCode):
    logger.info(f'------------------ TEST {testCode} ------------------')
    sesh = Session(logger,playerCount=2)
    players = ['Adam','Verina']
    for i in range(len(players)):
        sesh.players[i].name = players[i]
    sesh.newGame()

    if testCode == 1: #full house and pair  test
        sesh.players[0].hand[0] = Card('H',12)
        sesh.players[0].hand[1] = Card('S',12)

        sesh.players[1].hand[0] = Card('C',10)
        sesh.players[1].hand[1] = Card('D',8)

        sesh.COMMUNITY_CARDS[0] = Card('D',10)
        sesh.COMMUNITY_CARDS[1] = Card('S',10)
        sesh.COMMUNITY_CARDS[2] = Card('C',8)
        sesh.COMMUNITY_CARDS[3] = Card('D',7)
        sesh.COMMUNITY_CARDS[4] = Card('C',12)
    elif testCode == 2: # 2 pockets
        sesh.players[0].hand[0] = Card('H',12)
        sesh.players[0].hand[1] = Card('S',12)

        sesh.players[1].hand[0] = Card('C',10)
        sesh.players[1].hand[1] = Card('S',10)

        sesh.COMMUNITY_CARDS[0] = Card('H',9)
        sesh.COMMUNITY_CARDS[1] = Card('S',4)
        sesh.COMMUNITY_CARDS[2] = Card('C',8)
        sesh.COMMUNITY_CARDS[3] = Card('D',7)
        sesh.COMMUNITY_CARDS[4] = Card('C',13)

    elif testCode == 3: #flush test
        sesh.players[0].hand[0] = Card('H',12)
        sesh.players[0].hand[1] = Card('S',12)

        sesh.players[1].hand[0] = Card('D',10)
        sesh.players[1].hand[1] = Card('D',8)

        sesh.COMMUNITY_CARDS[0] = Card('H',10)
        sesh.COMMUNITY_CARDS[1] = Card('C',10)
        sesh.COMMUNITY_CARDS[2] = Card('C',8)
        sesh.COMMUNITY_CARDS[3] = Card('D',7)
        sesh.COMMUNITY_CARDS[4] = Card('C',12)
    elif testCode == 4:#straight test
        sesh.players[0].hand[0] = Card('S',12)
        sesh.players[0].hand[1] = Card('C',11)

        sesh.players[1].hand[0] = Card('D',10)
        sesh.players[1].hand[1] = Card('D',8)

        sesh.COMMUNITY_CARDS[0] = Card('S',10)
        sesh.COMMUNITY_CARDS[1] = Card('D',9)
        sesh.COMMUNITY_CARDS[2] = Card('C',8)
        sesh.COMMUNITY_CARDS[3] = Card('D',7)
        sesh.COMMUNITY_CARDS[4] = Card('C',12)
    elif testCode == 5: #regular straight test 1
        sesh.players[0].hand[0] = Card('S',12)
        sesh.players[0].hand[1] = Card('C',11)

        sesh.players[1].hand[0] = Card('D',10)
        sesh.players[1].hand[1] = Card('D',8)

        sesh.COMMUNITY_CARDS[0] = Card('S',10)
        sesh.COMMUNITY_CARDS[1] = Card('D',9)
        sesh.COMMUNITY_CARDS[2] = Card('C',8)
        sesh.COMMUNITY_CARDS[3] = Card('D',7)
        sesh.COMMUNITY_CARDS[4] = Card('C',12)
    elif testCode == 6: #ace high straight test
        sesh.players[0].hand[0] = Card('S',14)
        sesh.players[0].hand[1] = Card('C',2)

        sesh.players[1].hand[0] = Card('D',10)
        sesh.players[1].hand[1] = Card('D',8)

        sesh.COMMUNITY_CARDS[0] = Card('S',13)
        sesh.COMMUNITY_CARDS[1] = Card('D',12)
        sesh.COMMUNITY_CARDS[2] = Card('C',11)
        sesh.COMMUNITY_CARDS[3] = Card('D',7)
        sesh.COMMUNITY_CARDS[4] = Card('C',10)

    elif testCode == 7: # ace low straight test
        sesh.players[0].hand[0] = Card('S',14)
        sesh.players[0].hand[1] = Card('C',2)

        sesh.players[1].hand[0] = Card('D',10)
        sesh.players[1].hand[1] = Card('D',8)

        sesh.COMMUNITY_CARDS[0] = Card('S',3)
        sesh.COMMUNITY_CARDS[1] = Card('D',4)
        sesh.COMMUNITY_CARDS[2] = Card('C',5)
        sesh.COMMUNITY_CARDS[3] = Card('D',6)
        sesh.COMMUNITY_CARDS[4] = Card('C',10)
    elif testCode == 8: # straight flush test
        sesh.players[0].hand[0] = Card('S',14)
        sesh.players[0].hand[1] = Card('S',2)

        sesh.players[1].hand[0] = Card('D',10)
        sesh.players[1].hand[1] = Card('D',8)

        sesh.COMMUNITY_CARDS[0] = Card('S',3)
        sesh.COMMUNITY_CARDS[1] = Card('S',4)
        sesh.COMMUNITY_CARDS[2] = Card('S',5)
        sesh.COMMUNITY_CARDS[3] = Card('D',6)
        sesh.COMMUNITY_CARDS[4] = Card('C',10)
    elif testCode == 9: # straight flush test - double card value numbers
        sesh.players[0].hand[0] = Card('D',10)
        sesh.players[0].hand[1] = Card('D',8)
        sesh.players[1].hand[0] = Card('C',6)
        sesh.players[1].hand[1] = Card('C',2)

        sesh.COMMUNITY_CARDS[0] = Card('C',3)
        sesh.COMMUNITY_CARDS[1] = Card('C',4)
        sesh.COMMUNITY_CARDS[2] = Card('C',5)
        sesh.COMMUNITY_CARDS[3] = Card('D',7)
        sesh.COMMUNITY_CARDS[4] = Card('C',10)
    elif testCode == 10: # royal flush test 1
        sesh.players[0].hand[0] = Card('D',10)
        sesh.players[0].hand[1] = Card('D',12)
        sesh.players[1].hand[0] = Card('C',6)
        sesh.players[1].hand[1] = Card('C',2)

        sesh.COMMUNITY_CARDS[0] = Card('D',14)
        sesh.COMMUNITY_CARDS[1] = Card('D',11)
        sesh.COMMUNITY_CARDS[2] = Card('D',2)
        sesh.COMMUNITY_CARDS[3] = Card('D',7)
        sesh.COMMUNITY_CARDS[4] = Card('D',13)

    elif testCode == 11: # royal flush test 2
        sesh.players[0].hand[0] = Card('D',10)
        sesh.players[0].hand[1] = Card('D',12)
        sesh.players[1].hand[0] = Card('C',8)
        sesh.players[1].hand[1] = Card('C',2)

        sesh.COMMUNITY_CARDS[0] = Card('D',14)
        sesh.COMMUNITY_CARDS[1] = Card('D',11)
        sesh.COMMUNITY_CARDS[2] = Card('C',10)
        sesh.COMMUNITY_CARDS[3] = Card('D',7)
        sesh.COMMUNITY_CARDS[4] = Card('D',13)
    else:
        testCode = 99 #play a random game

    if 1 <= testCode <= 99: # use these codes for hand ranking tests
        sesh.showState()
        res = sesh.getBestHands()
        sesh.logger.info(f'result: {res}')

    end = time.clock()
    print(f'Total runtime: {end-start}')

if __name__ == '__main__':
    try:
        runTest(int(sys.argv[1]))
    except IndexError:
        main(0)
