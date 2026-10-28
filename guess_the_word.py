# Kevin Bell
# CIS256 Fall 2026
# Programming Assignment 4


#referenc urls:
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



import random


wordlist = [
    'skiing', 'skateboarding', 'dancing',
    'windsurfing', 'parachuting', 'corgi',
    'promotion', 'freestyle', 'butterfly',
    'community', 'assonance', 'baseline',
    'alliteration', 'underwater', 'iceberg',
    'stalactites', 'exceptional', 'privilege',
    'pressure', 'outstanding', 'preparation'
    ]


def shuffle_random():
    random.shuffle(wordlist)
    return wordlist

   
def show_random():
    some_random = random.choice(shuffle_random())
    return some_random


def show_combined(rand_word: str):
    rwlength = len(rand_word)
    display = ("_" * rwlength)
    space = ' '
    combined = space.join(display)
    return combined


def compare_guess(guess):
    #guess = 's'
    vowels = 'aeiouy'
    #letters = 'bnps'
    consonants = 'bcdfghjklmpqrstvwxz'
    #for guess in display:
    for letter in display:
        if letter in guess:
        #if guess in vowels or guess in consonants:
        #if guess in letter:
            print(guess, end=" ")
        else:
            print("_", end=" ")
    #attempts -= 1
    #print(f"\nYou have {attempts} attempts left!\n")
    

print()
#print("\n\n")
#print()

#str variable random_word
#assigned show_random()
#return value
random_word = show_random()

#visual validation
print(random_word)

#print(len(random_word))
print()




#str variable billboard
#displays underscores for
#each random_word letter
billboard = show_combined(random_word)
#print(billboard)
print(f"billboard is: \n{billboard}")
#print(len(billboard))

#keep count of "_" in billboard variable
#to signal when the word has been guessed!
uscore = billboard.count("_")
#print(uscore)


#initialize attempts outside while loop!
attempts = 15


#keep track of letters guessed
#has to be initialized outside
#loop or it resets each iteration
tracker = ''


#while loop until word
#is guessed correctly!
while True:
    
    #visual validation
    print(f"attempts left is {attempts}")
    #visual validation
    print(F"uscore is {uscore}")
    
    if (attempts >= 1) and (uscore >= 1):
        try:
            uscore = billboard.count("_")
            #print(uscore)
            guess = input(str("\nEnter a letter to guess the word: "))
            if not isinstance(guess, str):
                raise ValueError("not a letter!")
        except ValueError as e:
            print("{e}: Please enter a valid letter")
            
        print(guess)

        #add your guess to the str variable
        #tracker to help in persisting billboard
        tracker += guess

        #visual validation
        print(f"tracker is: {tracker}")
            #compare_guess(guess)

        #check each letter
        #in the random_word
        for letter in random_word:

            #if the letter is in
            #the str variable tracker
            #print the letter
            if letter in tracker:
                print(letter, end=" ")
                
                #decrement uscore to
                #validate word has
                #been guessed!
                uscore -= 1

            #else print an underscore
            #billboard still retains
            #its initial chars from
            #show_combined function
            else:
                print("_", end=" ")

        #countdown number of
        #attempts progress
        attempts -= 1
        
    #elif uscore < 1:
    #cover else for testing
    elif not (uscore >= 1):
        #uscore == 0:
        #uscore < 1:
        print("Great job! You guessed the word!")
        break
    
    #else attempts < 1:
    #cover else for testing
    elif not (attempts >= 1):
        #attempts < 1:
        print("You're out of guesses!")
        print(f"..but the word is {random_word}")
        break

    #display number of billboard
    #dashes left to uncover
    print(f"\nbillboard has {uscore} dashes left")

    #display number of
    #attempts left
    print(f"\nYou have {attempts} attempts left!\n") 
        

#
#parachuting
#
#billboard is: 
#_ _ _ _ _ _ _ _ _ _ _
#attempts left is 11
#uscore is 11
#11
#
#Enter a letter to guess the word: a
#a
#tracker is: a
#_ a _ a _ _ _ _ _ _ _ 
#billboard has 9 dashes left
#
#You have 10 attempts left!
#
#attempts left is 10
#uscore is 9
#11
#
#Enter a letter to guess the word: i
#i
#tracker is: ai
#_ a _ a _ _ _ _ i _ _ 
#billboard has 8 dashes left
#
#You have 9 attempts left!
#
#attempts left is 9
#uscore is 8
#11
#
#Enter a letter to guess the word: u
#u
#tracker is: aiu
#_ a _ a _ _ u _ i _ _ 
#billboard has 7 dashes left
#
#You have 8 attempts left!
#
#attempts left is 8
#uscore is 7
#11
#
#Enter a letter to guess the word: p
#p
#tracker is: aiup
#p a _ a _ _ u _ i _ _ 
#billboard has 6 dashes left
#
#You have 7 attempts left!
#
#attempts left is 7
#uscore is 6
#11
#
#Enter a letter to guess the word: r
#r
#tracker is: aiupr
#p a r a _ _ u _ i _ _ 
#billboard has 5 dashes left
#
#You have 6 attempts left!
#
#attempts left is 6
#uscore is 5
#11
#
#Enter a letter to guess the word: c
#c
#tracker is: aiuprc
#p a r a c _ u _ i _ _ 
#billboard has 4 dashes left
#
#You have 5 attempts left!
#
#attempts left is 5
#uscore is 4
#11
#
#Enter a letter to guess the word: h
#h
#tracker is: aiuprch
#p a r a c h u _ i _ _ 
#billboard has 3 dashes left
#
#You have 4 attempts left!
#
#attempts left is 4
#uscore is 3
#11
#
#Enter a letter to guess the word: t
#t
#tracker is: aiuprcht
#p a r a c h u t i _ _ 
#billboard has 2 dashes left
#
#You have 3 attempts left!
#
#attempts left is 3
#uscore is 2
#11
#
#Enter a letter to guess the word: n
#n
#tracker is: aiuprchtn
#p a r a c h u t i n _ 
#billboard has 1 dashes left
#
#You have 2 attempts left!
#
#attempts left is 2
#uscore is 1
#11
#
#Enter a letter to guess the word: g
#g
#tracker is: aiuprchtng
#p a r a c h u t i n g 
#billboard has 0 dashes left
#
#You have 1 attempts left!
#
#attempts left is 1
#uscore is 0
#You guessed the word!
#


#
#Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
#Enter "help" below or click "Help" above for more information.
#
#============= RESTART: C:\Users\midcw\Desktop\PA4\guess_the_word.py ============
#
#privilege
#
#billboard is: 
#_ _ _ _ _ _ _ _ _
#attempts left is 15
#uscore is 9
#
#Enter a letter to guess the word: a
#a
#tracker is: a
#_ _ _ _ _ _ _ _ _ 
#billboard has 9 dashes left
#
#You have 14 attempts left!
#
#attempts left is 14
#uscore is 9
#
#Enter a letter to guess the word: e
#e
#tracker is: ae
#_ _ _ _ _ _ e _ e 
#billboard has 7 dashes left
#
#You have 13 attempts left!
#
#attempts left is 13
#uscore is 7
#
#Enter a letter to guess the word: i
#i
#tracker is: aei
#_ _ i _ i _ e _ e 
#billboard has 5 dashes left
#
#You have 12 attempts left!
#
#attempts left is 12
#uscore is 5
#
#Enter a letter to guess the word: o
#o
#tracker is: aeio
#_ _ i _ i _ e _ e 
#billboard has 5 dashes left
#
#You have 11 attempts left!
#
#attempts left is 11
#uscore is 5
#
#Enter a letter to guess the word: u
#u
#tracker is: aeiou
#_ _ i _ i _ e _ e 
#billboard has 5 dashes left
#
#You have 10 attempts left!
#
#attempts left is 10
#uscore is 5
#
#Enter a letter to guess the word: r
#r
#tracker is: aeiour
#_ r i _ i _ e _ e 
#billboard has 4 dashes left
#
#You have 9 attempts left!
#
#attempts left is 9
#uscore is 4
#
#Enter a letter to guess the word: l
#l
#tracker is: aeiourl
#_ r i _ i l e _ e 
#billboard has 3 dashes left
#
#You have 8 attempts left!
#
#attempts left is 8
#uscore is 3
#
#Enter a letter to guess the word: p
#p
#tracker is: aeiourlp
#p r i _ i l e _ e 
#billboard has 2 dashes left
#
#You have 7 attempts left!
#
#attempts left is 7
#uscore is 2
#
#Enter a letter to guess the word: v
#v
#tracker is: aeiourlpv
#p r i v i l e _ e 
#billboard has 1 dashes left
#
#You have 6 attempts left!
#
#attempts left is 6
#uscore is 1
#
#Enter a letter to guess the word: g
#g
#tracker is: aeiourlpvg
#p r i v i l e g e 
#billboard has 0 dashes left
#
#You have 5 attempts left!
#
#attempts left is 5
#uscore is 0
#You guessed the word!
#
