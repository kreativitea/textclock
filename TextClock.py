#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import itertools
import collections

NUMBERS = dict(enumerate(
    'TWELVE ONE TWO THREE FOUR _FIVE SIX SEVEN EIGHT NINE _TEN ELEVEN TWELVE'
    .split()))


class Word(collections.namedtuple('Word', 'row start end')):
    def render(face):
        return face[self.row][self.start:self.end]


face = [f.strip() for f in """
    ITLISASTIME
    ACQUARTERDC
    TWENTYFIVEX
    HALFBTENFTO
    PASTERUNINE
    ONESIXTHREE
    FOURFIVETWO
    EIGHTELEVEN
    SEVENTWELVE
    TENSEOCLOCK
    """.split()]

mapping = {
    'IT':  Word(0, 0, 2),
    'IS':  Word(0, 3, 5),
    'A':  Word(1, 0, 1),
    'QUARTER':  Word(1, 2, 9),
    'TWENTY': Word(2, 0, 6),
    'FIVE':  Word(2, 6, 10),
    'TWENTYFIVE':  Word(2, 0, 10),
    'HALF':  Word(3, 0, 4),
    'TEN':  Word(3, 5, 8),
    'TO':  Word(3, 9, 11),
    'PAST':  Word(4, 0, 4),
    'NINE':  Word(4, 7, 11),
    'ONE':  Word(5, 0, 3),
    'SIX':  Word(5, 3, 6),
    'THREE':  Word(5, 6, 11),
    'FOUR':  Word(6, 0, 4),
    '_FIVE':  Word(6, 4, 8),
    'TWO':  Word(6, 8, 11),
    'EIGHT':  Word(7, 0, 5),
    'ELEVEN':  Word(7, 5, 11),
    'SEVEN':  Word(8, 0, 5),
    'TWELVE':  Word(8, 5, 11),
    '_TEN':  Word(9, 0, 3),
    'OCLOCK':  Word(9, 5, 11),
}


def xy(word):
    _word = mapping[word.upper()]
    return itertools.product([_word.row], range(_word.start, _word.end))


def render(t=None):
    time_string = gentime(now=t)
    for word in time_string.split():
        for coordinate in xy(word.strip()):
            id = len(face[0]) * coordinate[0] + coordinate[1]
            yield (id, ) + coordinate


STATEMENT = 'IT IS'


gen_mapping = {
    0: lambda hour: '{} {} {}'.format(STATEMENT, this_hour(hour), 'OCLOCK'),
    60: lambda hour: '{} {} {}'.format(STATEMENT, next_hour(hour), 'OCLOCK'),
    30: lambda hour: '{} {} {}'.format(STATEMENT, 'HALF PAST', this_hour(hour)),
    15: lambda hour: '{} {} {}'.format(STATEMENT, 'A QUARTER PAST', this_hour(hour)),
    45: lambda hour: '{} {} {}'.format(STATEMENT, 'A QUARTER TO', next_hour(hour)),
    5: lambda hour: '{} {} {}'.format(STATEMENT, 'FIVE PAST', this_hour(hour)),
    55: lambda hour: '{} {} {}'.format(STATEMENT, 'FIVE TO', next_hour(hour)),
    10: lambda hour: '{} {} {}'.format(STATEMENT, 'TEN PAST', this_hour(hour)),
    50: lambda hour: '{} {} {}'.format(STATEMENT, 'TEN TO', next_hour(hour)),
    25: lambda hour: '{} {} {}'.format(STATEMENT, 'TWENTYFIVE PAST', this_hour(hour)),
    35: lambda hour: '{} {} {}'.format(STATEMENT, 'TWENTYFIVE TO', next_hour(hour)),
    20: lambda hour: '{} {} {}'.format(STATEMENT, 'TWENTY PAST', this_hour(hour)),
    40: lambda hour: '{} {} {}'.format(STATEMENT, 'TWENTY TO', next_hour(hour))
    }


def gentime(now=None):
    ''' Creates a string representation of the current time. '''
    statement = 'IT IS'
    if not now:
        now = datetime.datetime.now()

    minute = round_time(now)
    hour = now.hour

    try:
        return gen_mapping[minute](hour)
    except KeyError:
        raise NotImplementedError


def round_time(dt):
    new_time = dt + datetime.timedelta(minutes=2, seconds=30)
    if new_time.minute // 5 == dt.minute // 5:
        return (dt.minute // 5) * 5
    else:
        return ((dt.minute // 5) * 5) + 5


def this_hour(hour):
    return NUMBERS[hour % 12]


def next_hour(hour):
    return NUMBERS[(hour + 1) % 12]
