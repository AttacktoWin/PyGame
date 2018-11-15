import random
HANGMAN_PICS = ['''
  3.   +---+
  4.       |
  5.       |
  6.       |
  7.      ===''', '''
  8.   +---+
  9.   O   |
 10.       |
 11.       |
 12.      ===''', '''
 13.   +---+
 14.   O   |
 15.   |   |
 16.       |
 17.      ===''', '''
 18.   +---+
 19.   O   |
 20.  /|   |
 21.       |
 22.      ===''', '''
 23.   +---+
 24.   O   |
 25.  /|\  |
 26.       |
 27.      ===''', '''
 28.   +---+
 29.   O   |
 30.  /|\  |
 31.  /    |
 32.      ===''', '''
 33.   +---+
 34.   O   |
 35.  /|\  |
 36.  / \  |
 37.      ===''']

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def getRandomWord(wordList):
    return wordList[random.randint(0, len(wordList) - 1)]

def display(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed Letters:', end='')
    for letter in missedLetters:
        print(letter, end='')
    print()

    blanks = '_ '*len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i+1] + secretWord[i] + blanks[i+3:]
    
    for letter in blanks:
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    jokes = False
    while True:
        print('Guess a letter:')
        guess = input().lower()
        if guess == 'letter' or guess == 'a letter':
            print('Haha, very funny, guess a character')
            jokes = True
        elif guess == 'character' and jokes or guess == 'a character' and jokes:
            print('>:(')
        elif len(guess) != 1:
            print('Just ONE letter:')
        elif guess in alreadyGuessed:
            print('You already guessed ' + guess + '. Please guess a different letter:')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('No, a LETTER:')
        else:
            return guess

def playAgain():
    print('Do you want to play again?')
    return input().lower().startswith('y')


print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    display(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters += guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is ' + secretWord + '! You win!')
            gameIsDone = True
    else:
        missedLetters += guess

        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            display(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct ones, the word was ' + secretWord)
            gameIsDone = True
    
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            secretWord = getRandomWord(words)
            gameIsDone = False
        else:
            break