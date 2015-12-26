#!/usr/bin/env python
 
import time
 
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
 
def loop():
 
    GPIO.output(RED_LED, True)
    GPIO.output(GREEN_LED, False)
    time.sleep(MAIL_CHECK_FREQ)
    GPIO.output(RED_LED, False)
    GPIO.output(GREEN_LED, True)
    time.sleep(MAIL_CHECK_FREQ)
    GPIO.output(RED_LED, True)
    GPIO.output(GREEN_LED, True)
    time.sleep(MAIL_CHECK_FREQ)
    GPIO.output(RED_LED, False)
    GPIO.output(GREEN_LED, False)
    time.sleep(MAIL_CHECK_FREQ)
 
if __name__ == '__main__':
    try:
        print 'Press Ctrl-C to quit.'
        while True:
            loop()
    finally:
        GPIO.cleanup()
