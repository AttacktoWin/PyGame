import random

guesses = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1, 20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20')

for guesses in range(6):
    print('Take a guess: (guesses remaining ' + str(6 - guesses) + ')')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Nope, too low!')
    if guess > number:
        print('Nope, too high!')

    if guess == number:
        break

if guess == number:
    guesses = str(guesses + 1)
    number = str(number)
    print('Congrats, ' + myName + '! It was ' + number + '! It only took you ' + guesses + ' guesses!')

if guess != number:
    number = str(number)
    print('Sorry, the number I was thinking of was ' + number + '.')