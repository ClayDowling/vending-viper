#!/usr/bin/python3

import argparse
import RPi.GPIO as GPIO

def doIt(pin, direction):

    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, direction)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Control LEDs')
    parser.add_argument('pin', metavar='N', type=int, nargs='+', help='Pins to set')
    parser.add_argument('--low', action='store_true', help='Set pins low (default)')
    parser.add_argument('--high', action='store_true', help='Set pins high')

    args = parser.parse_args()

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    pinState = False
    if args.high:
        pinState = True

    for pin in args.pin:
        doIt(pin, pinState)
