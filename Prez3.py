
# Author: Chris Osborne
# Date: 01/18/2021
# Description: This program is an interpretation of how a robot might communicate.
#                   Connect the robot via the bluetooth dongle, open .py file, and run code.
#                   The computer will display a message to choose A or B, but the screen on the bot will also.
#                   Press and hold in your desired button. The bot will go through a thinking cycle, and then
#                   execute that branch of the code. After it has completed that, it will loop into the selection
#                   phase. At any point you may end the program by shining a bright light at the left side of the bot.

from time import sleep
from random import randint
from BirdBrain import Finch

bot = Finch()

# notes
A = 56
B = 58
C = 60
D = 62
E = 64
F = 66
G = 68

song = [G,G,A,G,C,B,G,G,A,G,D,C,G,G,G,E,C,B,A,F,F,E,C,D,E] #enter desired noted here

#letters to display on the screen (setdisplay method)
letA = [0,0,1,0,0, 0,1,0,1,0, 1,1,1,1,1, 1,0,0,0,1, 1,0,0,0,1]
letB = [1,1,1,1,0, 1,0,0,0,1, 1,1,1,1,0, 1,0,0,0,1, 1,1,1,1,0]

print("Please Press button 'A', or 'B':")

while not bot.getButton("B" or "A"):    #plays A or B sequence
    count = 0

    if count == 0: #initialize light sequence
        bot.stopAll()

    for i in range(1, 5):
        bot.playNote(42, 0.1)

        bot.setDisplay(letA) #display A
        sleep(0.5)

        bot.setTail(i, 100, 0, 0) #increase light
        sleep(0.001)
        count += 1

        bot.playNote(46, 0.1)

        bot.setDisplay(letB) #display B
        sleep(0.5)

        bot.setTail(i, 100, 0, 0) #increase light
        sleep(0.001)
        count += 1

    if count == 10: #reset light sequence
        bot.stopAll()


    if bot.getButton("B") == True:  #if button B is pushed
        count = 0

        while count < 3:
            for i in range(2, 4):
                bot.setDisplay(letB)  #display letter B
                sleep(0.1)

                bot.setTail(i, 0, 100, 0) #change light
                sleep(0.1)
                bot.stopAll()
                sleep(0.1)

                bot.playNote(46, 0.1)   #play note

            for j in range(4, 0, -1):
                bot.setDisplay(letB)  #display letter B
                sleep(0.1)

                bot.setTail(j, 0, 100, 0) #change light
                sleep(0.1)
                bot.stopAll()
                sleep(0.1)

                bot.playNote(46, 0.1)   #play note

            count += 1
        sleep(0.5)

        lights = 30 #initialize lights for counter
        while lights >= 0:  #play light sequence
            a = randint(0, 100)
            b = randint(0, 100)
            c = randint(0, 100)
            d = randint(0, 4)

            bot.setBeak(a, b, c)    #turns on beak light
            bot.setTail(d, a, b, c)  #turns on tail light
            sleep(0.4)

            if bot.getLight("L" or "R") > 10:   #quit program if a light is shined at it
                bot.stopAll()
                break

            lights -= 1

        if bot.getLight("L" or "R") > 10:   #quit program if a light is shined at it
            bot.stopAll()
            break

        bot.setBeak(0, 0, 0)

    elif bot.getButton("A") == True:  #if button A is pushed
        count = 0
        while count < 3:

            for i in range(2, 4):

                bot.setDisplay(letA)  #display letter A
                sleep(0.1)

                bot.setTail(i, 0, 100, 0)  #change light
                sleep(0.1)
                bot.stopAll()
                sleep(0.1)

                bot.playNote(56, 0.1)  # play note

            for j in range(4, 0, -1):
                bot.setDisplay(letA)  #display letter A
                sleep(0.1)

                bot.setTail(j, 0, 100, 0)  #change light
                sleep(0.1)
                bot.stopAll()
                sleep(0.1)

                bot.playNote(56, 0.1)  # play note

            count += 1

        sleep(0.5)
        for note in song:   #play song
            bot.playNote(note, 1)

            if bot.getLight("L" or "R") > 10:   #quit program if a light is shined at it
                bot.stopAll()
                break

            sleep(0.3)

        if bot.getLight("L" or "R") > 10:   #quit program if a light is shined at it
            bot.stopAll()
            break

    if bot.getLight("L" or "R") > 10:   #quit program if a light is shined at it
        bot.stopAll()
        break
