# Problem Set 2, hangman.py
# Name: Diana Shramko
# Group: KM-03
# Collaborators: by myself
# Time spent: one evening(about 4-5 hours)

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
import collections

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed = set(secret_word).issubset(letters_guessed)
    return guessed



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    already_guessed = ""
    for i in secret_word:
        if i in letters_guessed:
            already_guessed = already_guessed + i
        else:
            already_guessed = already_guessed + " _ "
    return already_guessed

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    result = string.ascii_lowercase
    allLettersList = []
    for c in result:
        allLettersList.append(c)
    for i in allLettersList:
        if i in letters_guessed:
            allLettersList.remove(i)
        else:
            pass
    allLettersList = "".join(allLettersList)
    return allLettersList



def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses_remaining = 6
    letters_guessed = []
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print("You have 3 warnings left.")
    print("---------------------------")
    print("You have " + str(guesses_remaining) + " guesses left.")
    print("Available letters: ", string.ascii_lowercase)
    warnings_remaining = 3
    while True:
        letter = input("Please guess a letter:").lower()
        if len(letter) != 1:
            warnings_remaining -= 1
            if warnings_remaining <= -1:
                guesses_remaining -= 1
                print("You have no warnings left.Now you have -1 guess.")
            else:
                print("You need to enter 1 letter. You have " + str(warnings_remaining) + " warnings left.")
        if letter.isalpha() == False:
            warnings_remaining -= 1
            if warnings_remaining <= -1:
                guesses_remaining -= 1
                print("You have no warnings left.Now you have -1 guess.")
            else:
                print("Oops! That is not a valid letter. You have " + str(warnings_remaining) + " warnings left:")
        else:
            letters_guessed.append(letter)
        secret_word = list(secret_word)
        if letter in secret_word:
            print("Good guess:")
        elif letter.isalpha() == False:
            pass
        else:
            print("Oops! That letter is not in my word.")
        print(get_guessed_word(secret_word, letters_guessed))
        if is_word_guessed(secret_word, letters_guessed) == True:
            total_score = len(secret_word) * guesses_remaining
            print("Congratulations, you won!Your total score for this game is: " + str(total_score))
            break
        print("---------------------------")
        if letter in secret_word:
            print("You have " + str(guesses_remaining) + " guesses left")
        else:
            if letter == "a" or letter == "o" or letter == "e" or letter == "i":
                guesses_remaining -= 2
                print("You have " + str(guesses_remaining) + " guesses left")
            elif letter.isalpha() == False:
                pass
                print("You have " + str(guesses_remaining) + " guesses left")
            else:
                guesses_remaining -= 1
                print("You have " + str(guesses_remaining) + " guesses left")
        if guesses_remaining <= 0:
            secret_word = "".join(secret_word)
            print("Sorry, you ran out of guesses. The word was " + str(secret_word))
            break
        print("Available letters:", get_available_letters(letters_guessed))


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.replace(" ", "")
    my_word = list(my_word)
    other_word = list(other_word)
    new_my_word = []
    new_other_word = []
    if len(my_word) == len(other_word):
        for i in range(len(my_word)):
            if my_word[i] == "_":
                pass
            else:
                new_my_word.append(my_word[i])
                new_other_word.append(other_word[i])
    else:
        return False
    if new_my_word == new_other_word:
        return True
    else:
        return False



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    hints = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            hints.append(word)
    if hints == []:
        print("No matches found.")
    else:
        print("Possible word matches are:" + ", ".join(hints))




def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses_remaining = 6
    letters_guessed = []
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print("You have 3 warnings left.")
    print("---------------------------")
    print("You have " + str(guesses_remaining) + " guesses left.")
    print("Available letters: ", string.ascii_lowercase)
    warnings_remaining = 3
    while True:
        letter = input("Please guess a letter:").lower()
        if len(letter) != 1:
            warnings_remaining -= 1
            if warnings_remaining <= -1:
                guesses_remaining -= 1
                print("You have no warnings left.Now you have -1 guess.")
            else:
                print("You need to enter 1 letter. You have " + str(warnings_remaining)+ " warnings left.")
        if letter == "*":
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        elif letter.isalpha() == False:
            warnings_remaining -= 1
            if warnings_remaining <= -1:
                guesses_remaining -= 1
                print("You have no warnings left.Now you have -1 guess.")
            else:
                print("Oops! That is not a valid letter. You have " + str(warnings_remaining) + " warnings left:")
        else:
            letters_guessed.append(letter)
        secret_word = list(secret_word)
        if letter in secret_word:
            print("Good guess:")
        elif letter.isalpha() == False:
            pass
        else:
            print("Oops! That letter is not in my word.")
        print(get_guessed_word(secret_word, letters_guessed))
        if is_word_guessed(secret_word, letters_guessed) == True:
            total_score = len(secret_word) * guesses_remaining
            print("Congratulations, you won!Your total score for this game is: " + str(total_score))
            break
        print("---------------------------")
        if letter in secret_word:
            print("You have " + str(guesses_remaining) + " guesses left")
        else:
            if letter == "a" or letter == "o" or letter == "e" or letter == "i":
                guesses_remaining -= 2
                print("You have " + str(guesses_remaining) + " guesses left")
            elif letter.isalpha() == False:
                print("You have " + str(guesses_remaining) + " guesses left")
                pass
            else:
                guesses_remaining -= 1
                print("You have " + str(guesses_remaining) + " guesses left")
        if guesses_remaining <= 0:
            secret_word = "".join(secret_word)
            print("Sorry, you ran out of guesses. The word was " + str(secret_word))
            break
        print("Available letters: ", get_available_letters(letters_guessed))



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
