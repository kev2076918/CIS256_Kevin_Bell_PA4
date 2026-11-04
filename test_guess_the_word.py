# Kevin Bell
# CIS256 Fall 2026
# Programming Assignment 4

import random
import pytest
from guess_the_word import wordlist, random_word, shuffle_random, show_random, show_combined

wordlist = [
    'skiing', 'skateboarding', 'dancing',
    'windsurfing', 'parachuting', 'corgi',
    'promotion', 'freestyle', 'butterfly',
    'community', 'assonance', 'baseline',
    'alliteration', 'underwater', 'iceberg',
    'stalactites', 'exceptional', 'privilege',
    'pressure', 'outstanding', 'preparation',
    'sentinel', 'sophisticated', 'superfluous',
    'practice', 'preparedness', 'extenuating',
    'deciduous', 'sprawling', 'interconnected'
    ]


#def test_shuffle_random():
#    random.shuffle(wordlist)
#    return wordlist

@pytest.fixture
#def test_shuffle_random(func):
def shuffle_random(func):
    '''
    return a shuffled wordlist of items
    to enhance a more random selection
    '''
    @wraps(func)
    def test_wrapper():
        random.shuffle(wordlist)
        result = func()
        return result
    return wrapper


#def test_show_random():
#    #assert random.choice(shuffle_random()) == 'stalactites'
#    #return random.choice(shuffle_random()) == 'stalactites'
#    result = random.choice(shuffle_random())
#    assert result in wordlist

@pytest.fixture
@shuffle_random 
#def test_show_random():
def show_random():
    '''
    return random word from wordlist
    list of words to guess
    '''
    #some_random = random.choice(wordlist)
    #return some_random
    result = random.choice(shuffle_random())
    assert result in wordlist
    #some_random = random.choice(wordlist)
    #return some_random
    #assert some_random in wordlist


def test_shuffle_random_in_show_random():
    assert shuffle_random in show_random


def test_show_combined(random_word: "test"):
    #_random_word = random_word
    rwlength = len(random_word)
    assert rwlength == 4
    display = ("_" * rwlength)
    space = ' '
    combined = space.join(display)
    #return combined
    assert combined == " _ _ _ _ "
