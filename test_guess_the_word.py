# Kevin Bell
# CIS256 Fall 2026
# Programming Assignment 4

import random
from guess_the_word import shuffle_random, show_random

wordlist = [
    'skiing', 'skateboarding', 'dancing',
    'windsurfing', 'parachuting', 'corgi',
    'promotion', 'freestyle', 'butterfly',
    'community', 'assonance', 'baseline',
    'alliteration', 'underwater', 'iceberg',
    'stalactites', 'exceptional', 'privilege',
    'pressure', 'outstanding', 'preparation'
    ]


def test_shuffle_random():
    random.shuffle(wordlist)
    return wordlist

def test_show_random():
    #assert random.choice(shuffle_random()) == 'stalactites'
    return random.choice(shuffle_random()) == 'stalactites'

