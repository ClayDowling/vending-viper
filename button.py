import RPi.GPIO as GPIO

class Button:

    _pin = 0

    def __init__(self, pin, callback_function):
        _pin = pin
        self._setup_watcher(callback_function)

    def __del__(self):
        GPIO.remove_event_detect(self._pin)

    def _setup_watcher(self, callback_function):
        GPIO.setup(self._pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(self._pin, GPIO.RISING, callback=callback_function, bouncetime=400)