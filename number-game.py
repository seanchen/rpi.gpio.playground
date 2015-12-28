#!/usr/bin/env python
 
import time
import random
 
import RPi.GPIO as GPIO
 
MAIL_CHECK_FREQ = 1 # check mail every 60 seconds
 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
# port for Green led
GREEN_LED = 18
# port for red led
RED_LED = 23
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)

the_number = random.randrange(1, 1001)
GPIO.output(RED_LED, False)
GPIO.output(GREEN_LED, False)
 
def loop():

    guess = int(raw_input('Guess the number: '))

    if guess == the_number:
        GPIO.output(RED_LED, True)
        GPIO.output(GREEN_LED, True)
        print('***********************YOU WIN********************')
        time.sleep(2)
        print('Play again ....')
        GPIO.cleanup()
        exit()
        #the_number = random.randrange(3, 101)
        #time.sleep(0.5)
    elif guess > the_number:
        GPIO.output(RED_LED, True)
        GPIO.output(GREEN_LED, False)
        #time.sleep(2)
    else:
        GPIO.output(RED_LED, False)
        GPIO.output(GREEN_LED, True)
        #time.sleep(2)
 
if __name__ == '__main__':
    try:
        print 'Press Ctrl-C to quit.'
        while True:
            loop()
    finally:
        GPIO.cleanup()
