####################################
#Name: Andrew Redfield
#Date: 5/15/18
#Description: RPi Activity #4: Simon Says
####################################

import RPi.GPIO as GPIO
from time import sleep
from random import randint
import pygame

DEBUG = False
pygame.init()

switches = [20, 16, 12, 26]
leds = [6, 13, 19, 21]
sounds = [pygame.mixer.Sound("one.wav"), pygame.mixer.Sound("two.wav"), pygame.mixer.Sound("three.wav"), pygame.mixer.Sound("four.wav")]

GPIO.setmode(GPIO.BCM)

GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(leds, GPIO.OUT)

def all_on():
    for i in leds:
        GPIO.output(leds, True)

def all_off():
    for i in leds:
        GPIO.output(leds, False)

def lose(seq):
    for i in range(4):
        all_on()
        sleep(0.5)
        all_off()
        sleep(0.5)
    if (len(seq) > 3):
        print"You made it to a sequence of {}".format(len(seq)-1)
    else:
        print"You didn't even make it to a single sequence."
##############################################################
seq = []

seq.append(randint(0,3))
seq.append(randint(0,3))
s

print "Welcome to Simon!"
print "Try to play the sequence back"
print "Press CTRL+C to exit"

try:
    while(True):
        seq.append(randint(0, 3))
        if (DEBUG):
            if (len(seq) > 3):
                print
            print "seq={}".format(seq)

        for s in seq:
            if (len(seq) == 3) or (len(seq) == 4):
                GPIO.output(leds[s], True)
                sounds[s].play()
                sleep(1)
                GPIO.output(leds[s], False)
                sleep(0.5)

            elif (len(seq) == 5) or (len(seq) == 6):
                GPIO.output(leds[s], True)
                sounds[s].play()
                sleep(0.9)
                GPIO.output(leds[s], False)
                sleep(0.4)

            elif (len(seq) == 7) or (len(seq) == 8) or (len(seq) == 9):
                GPIO.output(leds[s], True)
                sounds[s].play()
                sleep(0.8)
                GPIO.output(leds[s], False)
                sleep(0.3)

            elif (len(seq) == 10) or (len(seq) == 11) or (len(seq) == 12):
                GPIO.output(leds[s], True)
                sounds[s].play()
                sleep(0.7)
                GPIO.output(leds[s], False)
                sleep(0.25)

            elif (len(seq) == 13) or (len(seq) == 14):
                GPIO.output(leds[s], True)
                sounds[s].play()
                sleep(0.6)
                GPIO.output(leds[s], False)
                sleep(0.15)

            elif (len(seq) >= 15):
                GPIO.output(leds[s], False)
                sounds[s].play()
                sleep(0.6)
                GPIO.output(leds[s], False)
                sleep(0.15)


        switch_count = 0
        while (switch_count < len(seq)):
            pressed = False
            while (not pressed):
                for i in range (len(switches)):
                    while (GPIO.input(switches[i]) == True):
                        val = i
                        pressed = True
            if (DEBUG):
                print val,

            GPIO.output(leds[val], True)
            sounds[val].play()
            sleep(1)
            GPIO.output(leds[val], False)
            sleep(0.25)

            if (val != seq[switch_count]):
                lose(seq)
                GPIO.cleanup()
                exit(0)

            switch_count += 1

except KeyboardInterrupt:
    GPIO.cleanup()
