from enum import Enum
from collections import Counter

class PokerRanked(Enum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIRS = 2
    THREE_OF_A_KIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_A_KIND = 7
    STRAIGHT_FLUSH = 8
    ROYAL_FLUSH = 10


def getRank(cards):

    numbers = [item[0] for item in cards]
    
    if len(set(item[1] for item in cards)) == 1:

        if {10, 11, 12, 13, 1} == set(numbers):
            return PokerRanked.ROYAL_FLUSH, 1
    
        if min(numbers) + 4 == max(numbers):
            return PokerRanked.STRAIGHT_FLUSH, min(numbers)

    counter = Counter(numbers)

    if 4 in dict(counter).values():
        number = [ n for n, c in counter.items() if c == 4][0]
        return PokerRanked.FOUR_A_KIND, number
    
    if {3, 2} == set(dict(counter).values()):
        return PokerRanked.FULL_HOUSE,  [item[0] for item in counter.most_common()]
    
    if len(set(item[1] for item in cards)) == 1:
        return PokerRanked.FLUSH, max(number)
    
    if min(numbers) + 4 == max(numbers):
        return PokerRanked.STRAIGHT, min(numbers)

    if 3 in dict(counter).values():
        number = [ n for n, c in counter.items() if c == 3][0]
        return PokerRanked.THREE_OF_A_KIND, number
    
    counter2 = counter(dict(counter).values)
    if 2 in dict(counter2).values():
        return PokerRanked.TWO_PAIRS, \
            list(reversed(sorted([k for k,v in counter.iterms() if v == 2])))

    if 2 in dict(counter).values():
        number = [ n for n, c in counter.items() if c == 2][0]
        return PokerRanked.ONE_PAIR, number
    
    return PokerRanked.HIGH_CARD, max(numbers)
