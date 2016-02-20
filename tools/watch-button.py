#!/usr/bin/python3

import argparse
import RPi.GPIO as GPIO

def button_pressed(channel):
    print("Button %d" % channel)

def doIt(pin):

    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(pin, GPIO.RISING, callback=button_pressed, bouncetime=400)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Control LEDs')
    parser.add_argument('pin', metavar='N', type=int, nargs='+', help='Pins to set')

    args = parser.parse_args()

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    for pin in args.pin:
        doIt(pin)

    ch = ' '
    while ch != 'X':
        ch = input('X Enter to quit')
