
# Author: Chris Osborne
# Date: 01/27/2021
# Description: This program is for a robot to navigate a maze. The user should set the but down, start the program, and
#                    direct it through the maze using a laser. If at any point the bot gets too close to a wall, it will play a tune
#                    and shut down. Try to make it through an entire maze!

from time import sleep
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

song = [G,G,A,G,C,B,G,G,A,G,D,C,G,G,G,E,C,B,A,F,F,E,C,D,E]

while bot.getDistance() > 2:
    #direct the bot to turn right
    if bot.getLight("L") > 10:
        bot.setBeak(0, 0, 100)  # Blue
        bot.setMotors(5, -5)
        # print("Left light sensor: ", bot.getLight("L"))

    # direct the bot to turn left
    elif bot.getLight("R") > 10:
        bot.setBeak(100, 0, 0)  # Red
        bot.setMotors(-5, 5)
        # print("right light sensor: ", bot.getLight("R"))

    # will drive strait unless given a direction
    else:
        bot.setBeak(0, 100, 0)  # Green
        bot.setMotors(3, 3)

#Play tune and end program
bot.setMotors(0, 0)
for note in song:  # play song
    bot.playNote(note, 1)
    sleep(.2)

bot.stopAll()























