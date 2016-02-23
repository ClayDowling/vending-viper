from time import sleep

class LED:

    _pin = 0

    def __init__(self, pin):
        import RPi.GPIO as GPIO
        self._pin = pin
        GPIO.setup(self._pin, GPIO.OUT)

    def blink(self, times, delay):
        import RPi.GPIO as GPIO
        for i in range(times):
            GPIO.output(self._pin, True)
            sleep(delay)
            GPIO.output(self._pin, False)
            sleep(delay)

    def turn_on(self):
        import RPi.GPIO as GPIO
        GPIO.output(self._pin, GPIO.HIGH)

    def turn_off(self):
        import RPi.GPIO as GPIO
        GPIO.output(self._pin, GPIO.LOW)