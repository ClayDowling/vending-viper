import led

class Dispenser:
    """
    Handle the dispensing of product.
    """

    _dispense_led = None

    def __init__(self, pin, ledOverride = None):
        dispensed_led = ledOverride
        if None == dispensed_led:
            self._dispense_led = led.LED(pin)

    def dispense_product(self, product):
        """
        Physically dispense the product.

        :param product: item to dispense
        :return: boolean, true if product dispensed, false otherwise
        """

        self._dispense_led.blink(10, 0.1)
        self._dispense_led.turn_off()

        return False