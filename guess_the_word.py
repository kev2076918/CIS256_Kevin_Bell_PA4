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
    

#print()
#str variable random_word
#assigned show_random()
#return value
random_word = show_random()

#visual validation
#print(random_word)

#print(len(random_word))
print()




#str variable billboard
#displays underscores for
#each random_word letter
billboard = show_combined(random_word)
#print(billboard)
#print(f"billboard is: \n{billboard}")
print(f"\n{billboard}")
#print(len(billboard))

#keep count of "_" in billboard variable
#to signal when the word has been guessed!
uscore = billboard.count("_")
#print(uscore)


#initialize attempts
#outside while loop!
attempts = 15


#keep track of letters guessed
#has to be initialized outside
#loop or it resets each iteration
tracker = ''


#while loop until word
#is guessed correctly!
while True:
    
    #visual validation
    #print(f"attempts left is {attempts}")
    #visual validation
    #print(F"uscore is {uscore}")

    #be sure both attempts are available
    #and billboard underscores are present
    if (attempts >= 1) and (uscore >= 1):
        try:
            uscore = billboard.count("_")
            #print(uscore)
            guess = input(str("\nEnter a letter to guess the word: "))
            if not isinstance(guess, str):
                raise ValueError("not a letter!")
        except ValueError as e:
            print("{e}: Please enter a valid letter")

        #visual validation
        #print(guess)

        #add your guess to the str variable
        #tracker to help in persisting billboard
        tracker += guess

        #visual validation
        #print(f"tracker is: {tracker}")

        #check each letter
        #in the random_word
        for letter in random_word:

            #if the letter is in
            #the str variable tracker
            #print the letter
            if letter in tracker:
                print(letter, end=" ")
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
    #print(f"\nbillboard has {uscore} dashes left")

    #display number of
    #attempts left
    print(f"\nYou have {attempts} attempts left!\n")
