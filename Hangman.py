###*********************************
#      HANGMAN GAME
# author: Taylor McPherson
# date: 6.27.18
# 
# My first personal project.
# A recreation of hangman.
# 
###***********************************
import string
from random import randint

#GLOBAL VARIABLES
hangWord = ""
lineWord = ""
wordList = []
triesLeft = 6

#generates hangman dictionary from Feminist_Dictionary.txt file
#and stores in wordList
def getWordList():
    with open("Feminist_Dictionary.txt", "r") as my_file:
        for x in my_file.readlines():
            wordList.append(x)
        my_file.close()
    return wordList

#randomly selects a word out of wordList 
def getWord():
    global hangWord
    hangword = ""
    length = len(wordList)
    wordIndex = randint(0, length-1)
    hangWord = wordList[wordIndex]
    hangWord = hangWord.lower()
    return hangWord
 
        
#gives opening message and explain how to play the game
#returns true when the game still goes on
#returns false when player is done playing
def hello():
    print ""
    print "*** WELCOME TO FEMINIST HANGMAN ****"
    print ""


#asks user if they want to play a new game
#ends gracefully if user is done playing
def newGame():
    print ""
    new_game = input("Ready to play a game? (yes = 1, no = 0)")

    if new_game == 1:
        know_how = input("  Do you know how to play? (yes = 1, no = 0) ")
        if know_how == 1:
            print "  Awesome! Let's start! "
            print ""     
        #explain how to play
        else:
            print "  Here\'s how we play... "
            print ""
            instructions()
        return True

    #no more games
    else:
        print ""
        print "*** THANKS FOR PLAYING, YOU INTERSECTIONAL SUPERSTAR ***"
        print ""
        print "            ****** Bye now! *******"
        print ""
        return False

#instructions for a user who does not know how to play
def instructions():
    print "The goal of the game is to guess my mystery word."
    print "I have a word bank of feminist buzzwords." + \
     " That's where your mystery word will come from."
    print "You will have 6 safety nets --"
    print "   This means if you guess a wrong letter, you lose" + \
     " one of your 6 safety nets."
    print " "
    print "If you guess the word before you run out of safety nets, you win!"
    print "Otherwise, you lose. But you can always play again!"
    print ""
    print "Got it? Great. Let\'s get started!"
    print ""
    
#create the starting underscores/lines that represent letters in hidden word
def startLines(word):
    global lineWord
    lineWord = ""
    for letter in range(len(word)-1):
        if letter == "-":
            lineWord += "-"
        elif letter == "+":
            lineWord += "+"
        else:
            lineWord += "_"
    return lineWord  

#once user guesses a letter, update what they see accordingly
def updateLines(guess):
    global hangWord
    global lineWord
    global triesLeft
    
    #account for repeat guesses
    if str(guess) in lineWord:
        print "You already guessed that letter."
        #print lineWord
        
        
    #to update lineWord if guess is correct
    if str(guess) in hangWord:
        for num in range(len(hangWord)-1):
            if hangWord[num] == guess:
                lineWord = replace_str_index(lineWord, num, guess)
        if "_" not in lineWord:
            lineWord = "done"
        print lineWord
    
    #account for incorrect guesses
    if str(guess) not in  hangWord:
        print str(guess) + " is not in your word."
        print lineWord
        triesLeft -= 1
        
    #update message output regarding amount of tries left
    if triesLeft == 0:
        #print lineWord
        lineWord = "stop"
    if triesLeft > 1:
        print "You have " + str(triesLeft) + " safety nets left." 
    if triesLeft == 1:
        print "You have " + str(triesLeft) + " safety net left." 
        
    return lineWord           
    
#user guesses letter
def guessLetter():
    print ""
    guess = raw_input("Guess a letter: ")
    print ""
    return str(guess)

#a quick way to replace a string index
def replace_str_index(string, index=0, replacement= " "):
    return "%s%s%s" % (string[:index], replacement, string[index+1:])

#to continually guess until user wins or loses
def guess():
    global lineWord
    global hangWord
    keep_guessing = True
    while keep_guessing:
        if updateLines(guessLetter()) == "stop":
            print "Bummer. You're out of guesses! "
            print "Your word was " + hangWord.upper()
            keep_guessing = False
        elif updateLines(guessLetter()) == "done":
            print "Rock on! You win!"
            keep_guessing = False
        elif "_" not in lineWord:
            print "You win!"
            keep_guessing = False
        else: 
            updateLines(guessLetter())

def resetTries():
    global triesLeft
    triesLeft = 6
    return triesLeft
            
#pull it all together
def game():
    hello()
    while newGame():
        resetTries()
        getWordList()
        print "Here's what you've got to start with: "
        print startLines(getWord())
        print""
        guess()

        
#so terminal actually runs this         
game()