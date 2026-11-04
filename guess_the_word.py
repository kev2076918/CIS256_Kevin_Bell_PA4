# Kevin Bell
# CIS256 Fall 2026
# Programming Assignment 4


#reference urls:
#https://www.datacamp.com/tutorial/how-to-convert-a-list-to-a-string-in-python
#https://mimo.org/glossary/python/string-join-method
#https://stackoverflow.com/questions/493819/why-is-it-string-joinlist-instead-of-list-joinstring
#https://www.w3schools.com/python/python_try_except.asp
#https://docs.python.org/3/tutorial/errors.html
#https://python.readthedocs.io/fr/stable/library/random.html
#https://medium.com/@akshayheights/understanding-python-decorators-with-a-simple-analogy-3f31dd35f72b
#https://www.geeksforgeeks.org/python/how-to-use-while-true-in-python/
#https://www.toolsqa.com/python/python-while-loop/
#https://www.w3schools.com/python/ref_string_replace.asp
#https://www.geeksforgeeks.org/python/python-string-replace/
#https://realpython.com/replace-string-python/
#https://www.serveracademy.com/blog/python-replace-function
#https://docs.python.org/3/library/random.html
#https://discovery.cs.illinois.edu/guides/Python-Fundamentals/exploring-random/
#https://www.geeksforgeeks.org/python/python-random-module/
#https://www.merriam-webster.com/


import random
from functools import wraps

#--------------------------------------------
#list object wordlist holds as many words
#as creator would need for guess_the_word.py!
#--------------------------------------------
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


#--------------------------------------------
#shuffle_random returns a "shuffled"
#initial wordlist (as a deck of cards!)
#to enhance a more random selection
#--------------------------------------------
def shuffle_random(func):
    '''
    return a shuffled wordlist of items
    to enhance a more random selection
    '''
    @wraps(func)
    def wrapper():
        random.shuffle(wordlist)
        result = func()
        return result
    return wrapper


#--------------------------------------------
#show_random returns a random choice
#from the "shuffled" wordlist
#--------------------------------------------
@shuffle_random 
def show_random():
    '''
    return random word from wordlist
    list of words to guess
    '''
    some_random = random.choice(wordlist)
    return some_random


#--------------------------------------------
#show_combined returns str object combined
#consisting of spaces joined with the ("_")
#number of underscores matching the length
#of the random word
#--------------------------------------------
def show_combined(rand_word: str):
    '''
    return a str object consisting of spaces
    joined by a number underscores from the
    length of the random word from show_random()
    '''
    rwlength = len(rand_word)
    display = ("_" * rwlength)
    space = ' '
    combined = space.join(display)
    return combined


#--------------------------------------------
#str variable random_word assigned
#show_random() return value
#--------------------------------------------
random_word = show_random()
#print(random_word)


#--------------------------------------------
#str variable billboard assigned show_combined()
#return value #which displays "_" underscores
#masking random_word letters
#--------------------------------------------
billboard = show_combined(random_word)
#print(billboard)


#--------------------------------------------
#diplay title outside while loop to declare
#guess_the_word game!
#print(f"Guess the word has {len(random_word)}
#letters: \n\n{billboard}")
#--------------------------------------------
print(f"Guess The Word:\n({len(random_word)} letters) \n\n{billboard}")
#print(len(billboard))
#print(f"Billboard has {len(billboard)} letters")


#--------------------------------------------
#num variable uscore assigned the "_" counter
#of str variable billboard and must be 
#initialized outside while loop to evaluate
#initial condition as true: (uscore >= 1)
#used as a sentinal signaling when no more "_"
#exist, random_word has been correctly guessed!
#--------------------------------------------
uscore = billboard.count("_")
#print(uscore)


#--------------------------------------------
#require attempts initialized outside the
#loop or number resets each iteration and
#must pass inital condition: (attempts >= 1)
#--------------------------------------------
attempts = 15


#--------------------------------------------
#require tracking of all letters guessed
#has to be initialized outside the loop
#or string resets each iteration
#--------------------------------------------
marquee = ''


#--------------------------------------------
#while loop until word is guessed correctly!
#--------------------------------------------
while True:
    
    #visual validation
    #print(f"attempts left is {attempts}")
    #print(f"\n\n{attempts} attempts left")
    #visual validation
    #print(f"uscore is {uscore}")

    #--------------------------------------------
    #both available attempts and random_word still
    #unguessed letters must be true to continue
    #while loop; if either evaluates false,
    #it triggers a break from the loop!
    #--------------------------------------------
    if (attempts >= 1) and (uscore >= 1):
        try:
            #initial uscore validates number of unguessed letters
            uscore = billboard.count("_")
            #print(uscore)
            #str variable hunch is added to str variable marquee
            hunch = input(str(f"\nEnter one letter per hunch: "))
            #if hunch is not a str object
            #raise ValueError
            if not isinstance(hunch, str):
                raise ValueError("not a letter!")
        except ValueError as e:
            print("{e}: Please enter a valid letter")

        #print()
        #visual validation
        #display latest hunch!
        print(hunch)

        #--------------------------------------------
        #hunches added to str variable marquee persist
        #displaying matching random_word letters!
        #--------------------------------------------
        marquee += hunch
        #visual validation
        #display str variable marquee
        #to assist in guessing the letters!
        print(f"marquee is: {marquee}\n")
        print()
        #print(f"uscore is {uscore}")

        #--------------------------------------------
        #for each letter in the random_word ->
        #reveal random_word letters matching hunches
        #added to str variable marquee!
        #--------------------------------------------
        for letter in random_word:

            #--------------------------------------------
            #if the hunch added to str variable marquee
            #matches any letter in the random_word,
            #display that letter!
            #--------------------------------------------
            if letter in marquee:
                print(letter, end=" ")

                #--------------------------------------------
                #decrement "_" underscore count only
                #when correct letter is guessed!
                #--------------------------------------------
                uscore -= 1

            #--------------------------------------------
            #else, if hunch added to str variable marquee
            #does not match any random word letters,
            #display an underscore!
            #billboard still retains initial chars from
            #show_combined() function
            #--------------------------------------------
            else:
                print("_", end=" ")

        #--------------------------------------------
        #to track progress, each hunch will countdown
        #the number of attempts!
        #--------------------------------------------
        attempts -= 1
        

    #--------------------------------------------
    #test elif not to cover count for testing
    #--------------------------------------------
    elif not (uscore >= 1):
        print("\n\nGreat job! \nYou guessed the word!")
        print("Enter Ctrl + D to end")
        #break out of loop!
        break
    
    #--------------------------------------------
    #test elif not to cover count for testing
    #--------------------------------------------
    elif not (attempts >= 1):
        print("\nYou're out of guesses!")
        print(f"..but the word is {random_word}")
        print("Enter Ctrl + D to end")
        #break out of loop!
        break

    #--------------------------------------------
    #display number of billboard dashes to uncover
    #print(f"\nbillboard has {uscore} dashes left")
    #--------------------------------------------
    #print(f"\n{uscore} dashes left\n")
    #print("\n")

    #--------------------------------------------
    #display number of attempts left
    #print(f"\nYou have {attempts} attempts left!\n")
    #--------------------------------------------
    print(f"\n{attempts} attempts left!\n")
        
