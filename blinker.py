from time import sleep
import RPi.GPIO as GPIO

class Blinker:


    _pin = 0

    def __init__(self, pin):
        self._pin = pin
        GPIO.setup(self._pin, GPIO.OUT)

    def blink(self, times, delay):
        for i in range(times):
            GPIO.output(self._pin, False)
            sleep(delay)
            GPIO.output(self._pin, True)
            sleep(delay)