import random, time

def displayIntro():
    print('You are an adventurer in land filled with dragons. In front of you are two caves. On your map you see that one cave has untold treasures while the other has a dragon that will eat you alive! Unfortunately, you cannot tell which cave is which.')
    print()

def chooseCave():
    cave = ''
    while cave != 'left' and cave != 'right':
        print('Which cave will you go into? Left or Right?')
        cave = input().lower()
    
    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('You light your torch and in front of you is...')
    time.sleep(3)

    treasureCave = random.randint(1, 2)

    if chosenCave == 'left' and treasureCave == 1 or chosenCave == 'right' and treasureCave == 2:
        print('A giant pile of gold!')
    else:
        print('A GIANT DRAGON THAT EATS YOU WHOLE!')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print('Do you want to play again?')
    playAgain = input().lower()