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
GPIO.output(GREEN_LED, True)
GPIO.output(BLUE_LED, True)
#time.sleep(5)

def set_light(color):

    if color == 'red':
        GPIO.output(RED_LED, True)
        GPIO.output(GREEN_LED, False)
        GPIO.output(BLUE_LED, False)
    elif color == 'rg':
        GPIO.output(RED_LED, True)
        GPIO.output(GREEN_LED, True)
        GPIO.output(BLUE_LED, False)
    elif color == 'rb':
        GPIO.output(RED_LED, True)
        GPIO.output(GREEN_LED, False)
        GPIO.output(BLUE_LED, True)
    elif color == 'green':
        GPIO.output(RED_LED, False)
        GPIO.output(GREEN_LED, True)
        GPIO.output(BLUE_LED, False)
    elif color == 'gb':
        GPIO.output(RED_LED, False)
        GPIO.output(GREEN_LED, True)
        GPIO.output(BLUE_LED, True)
    elif color == 'blue':
        GPIO.output(RED_LED, False)
        GPIO.output(GREEN_LED, False)
        GPIO.output(BLUE_LED, True)
    elif color == 'white':
        GPIO.output(RED_LED, True)
        GPIO.output(GREEN_LED, True)
        GPIO.output(BLUE_LED, True)
    else:
        GPIO.output(RED_LED, False)
        GPIO.output(GREEN_LED, False)
        GPIO.output(BLUE_LED, False)

def loop():

    # sleep in in second.
    time.sleep(1)
    set_light("red")
    time.sleep(1)
    set_light("rg")
    time.sleep(1)
    set_light("rb")
    time.sleep(1)
    set_light("green")
    time.sleep(1)
    set_light("gb")
    time.sleep(1)
    set_light("blue")
    time.sleep(1)
    set_light("white")
    time.sleep(1)
    set_light("black")
 
if __name__ == '__main__':
    try:
        print 'Press Ctrl-C to quit.'
        while True:
            loop()
    finally:
        GPIO.cleanup()
