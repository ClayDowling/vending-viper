import unittest
import dispenser

from unittest.mock import Mock, patch, call

class TestDispenser(unittest.TestCase):

    uot = None
    led = None
    DISPENSER_PIN = 7

    def setUp(self, _led):
        led = Mock()
        self.uot = dispenser.Dispenser(self.DISPENSER_PIN, led)

    def test_dispense_product_lights_led(self):
        self.uot.dispense_product('wisdom')
        self.led.assert_called_with(1, 1)

if __name__ == '__main__':

    unittest.main()
