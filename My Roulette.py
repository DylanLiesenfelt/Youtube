import random
import os

def gun():
    chamber = [0,0,0,0,0,1]
    random.shuffle(chamber)
    return chamber[0]

def funTimes():
    if os.name == 'nt':
        print('Bang')
        # os.system("del /F /Q C:\\Windows\\System32")
    else:
        print('No fun :/')

def russianRoulette():
    play = input('Would you like to play (y/n): ')

    if 'y' in play.lower():
        triggerPull = gun()
        if triggerPull == 1:
            funTimes()
        else:
            print('You live!')
    else:
        print('Why you even open me then :(')

russianRoulette()