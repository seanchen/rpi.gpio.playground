#!/usr/bin/env python
 
import time
import random
 
import RPi.GPIO as GPIO
 
MAIL_CHECK_FREQ = 1 # check mail every 60 seconds
 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
# port for Green led
GREEN_LED = 23
# port for red led
RED_LED = 18
BLUE_LED = 24
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(BLUE_LED, GPIO.OUT)

the_number = random.randrange(1, 1001)
GPIO.output(RED_LED, False)
GPIO.output(GREEN_LED, False)
GPIO.output(BLUE_LED, False)

def set_light(color):

    if color == 'red':
        GPIO.output(RED_LED, True)
        GPIO.output(GREEN_LED, False)
        GPIO.output(BLUE_LED, False)
    elif color == 'green':
        GPIO.output(RED_LED, False)
        GPIO.output(GREEN_LED, True)
        GPIO.output(BLUE_LED, False)
    elif color == 'blue':
        GPIO.output(RED_LED, False)
        GPIO.output(GREEN_LED, False)
        GPIO.output(BLUE_LED, True)
    else:
        GPIO.output(RED_LED, False)
        GPIO.output(GREEN_LED, False)
        GPIO.output(BLUE_LED, False)

def loop():

    guess = int(raw_input('Guess the number: '))

    if guess == the_number:
        set_light('blue')
        print('***********************YOU WIN********************')
        print('Play again ....')
        time.sleep(2)
        GPIO.cleanup()
        exit()
        #the_number = random.randrange(3, 101)
        #time.sleep(0.5)
    elif guess > the_number:
        set_light('red')
        time.sleep(0.5)
        set_light('black')
        time.sleep(0.5)
        set_light('red')
        #time.sleep(2)
    else:
        set_light('green')
        time.sleep(0.5)
        set_light('black')
        time.sleep(0.5)
        set_light('green')
        #time.sleep(2)
 
if __name__ == '__main__':
    try:
        print 'Press Ctrl-C to quit.'
        while True:
            loop()
    finally:
        GPIO.cleanup()
