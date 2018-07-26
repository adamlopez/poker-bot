import time
start = time.clock()
from person import Card,Player
from session import Session
from logger import getLogger
import  sys
logger = getLogger()

def main(code):
    logger.info(f'------------------ TEST {code} ------------------')
    sesh = Session(logger,players=2)
    sesh.newGame()

    if code == 1: #full house and pair  test
        sesh.players[0].hand[0] = Card('H',12)
        sesh.players[0].hand[1] = Card('S',12)

        sesh.players[1].hand[0] = Card('C',10)
        sesh.players[1].hand[1] = Card('D',8)

        sesh.COMMUNITY_CARDS[0] = Card('S',10)
        sesh.COMMUNITY_CARDS[1] = Card('S',10)
        sesh.COMMUNITY_CARDS[2] = Card('C',8)
        sesh.COMMUNITY_CARDS[3] = Card('D',7)
        sesh.COMMUNITY_CARDS[4] = Card('C',12)
        sesh.getBestHands()
    elif code == 2: #regular game
        sesh.getBestHands()
    elif code == 3: #flush test
        sesh.players[0].hand[0] = Card('H',12)
        sesh.players[0].hand[1] = Card('S',12)

        sesh.players[1].hand[0] = Card('D',10)
        sesh.players[1].hand[1] = Card('D',8)

        sesh.COMMUNITY_CARDS[0] = Card('H',10)
        sesh.COMMUNITY_CARDS[1] = Card('C',10)
        sesh.COMMUNITY_CARDS[2] = Card('C',8)
        sesh.COMMUNITY_CARDS[3] = Card('D',7)
        sesh.COMMUNITY_CARDS[4] = Card('C',12)
        sesh.getBestHands()
    elif code == 4:#straight test
        sesh.players[0].hand[0] = Card('S',12)
        sesh.players[0].hand[1] = Card('C',11)

        sesh.players[1].hand[0] = Card('D',10)
        sesh.players[1].hand[1] = Card('D',8)

        sesh.COMMUNITY_CARDS[0] = Card('S',10)
        sesh.COMMUNITY_CARDS[1] = Card('D',9)
        sesh.COMMUNITY_CARDS[2] = Card('C',8)
        sesh.COMMUNITY_CARDS[3] = Card('D',7)
        sesh.COMMUNITY_CARDS[4] = Card('C',12)
        sesh.getBestHands()
    elif code == 5: #regular straight test 1
        sesh.players[0].hand[0] = Card('S',12)
        sesh.players[0].hand[1] = Card('C',11)

        sesh.players[1].hand[0] = Card('D',10)
        sesh.players[1].hand[1] = Card('D',8)

        sesh.COMMUNITY_CARDS[0] = Card('S',10)
        sesh.COMMUNITY_CARDS[1] = Card('D',9)
        sesh.COMMUNITY_CARDS[2] = Card('C',8)
        sesh.COMMUNITY_CARDS[3] = Card('D',7)
        sesh.COMMUNITY_CARDS[4] = Card('C',12)
        sesh.getBestHands()
    elif code == 6: #ace high straight test
        sesh.players[0].hand[0] = Card('S',14)
        sesh.players[0].hand[1] = Card('C',2)

        sesh.players[1].hand[0] = Card('D',10)
        sesh.players[1].hand[1] = Card('D',8)

        sesh.COMMUNITY_CARDS[0] = Card('S',13)
        sesh.COMMUNITY_CARDS[1] = Card('D',12)
        sesh.COMMUNITY_CARDS[2] = Card('C',11)
        sesh.COMMUNITY_CARDS[3] = Card('D',7)
        sesh.COMMUNITY_CARDS[4] = Card('C',10)
        sesh.getBestHands()
    end = time.clock()
    print(f'Total runtime: {end-start}')

if __name__ == '__main__':
    try:
        main(int(sys.argv[1]))
    except IndexError:
        main(0)
