import button
import dispenser
import led
import vendingMachine

class PhysicalPanel:

    _vm = None
    _dispenser = None
    _led_need_money = None
    _btn_nickel = None
    _btn_dime = None
    _btn_quarter = None
    _product = None

    _pin_nickel = None
    _pin_dime = None
    _pin_quarter = None


    def __init__(self, config):
        self._vm = vendingMachine.VendingMachine()
        self._dispenser = dispenser.Dispenser(config['dispenser_pin'])
        self._led_need_money = led.LED(config['need_money_pin'])

        self._pin_nickel = config['nickel_pin']
        self._pin_dime = config['dime_pin']
        self._pin_quarter = config['quarter_pin']

        self._btn_nickel = button.Button(self._pin_nickel, self._on_button_pushed)
        self._btn_dime = button.Button(self._pin_dime, self._on_button_pushed)
        self._btn_quarter = button.Button(self._pin_quarter, self._on_button_pushed)

    def accept_money(self, coin):
        self._vm.input_coin(coin)
        self.money_added()

    def item_selected(self):
        self.check_purchase_state()

    def money_added(self):
        print("Total: %4.2f" % self._vm.get_coins_value())
        if None == self._product:
            return
        self.check_purchase_state()

    def check_purchase_state(self):
        if None == self._product:
            return
        if self._vm.can_purchase(self._product):
            self._enough_money_added()
        else:
            self._not_enough_money_added()

    def _not_enough_money_added(self):
        self._led_need_money.turn_on()

    def _enough_money_added(self):
        self._led_need_money.turn_off()
        self._dispenser.dispense_product(self._product)
        self._vm.purchase_product(self._product)
        self._product = None

    def _on_button_pushed(self, channel):
        if channel == self._pin_nickel:
            self.accept_money('nickel')
        if channel == self._pin_dime:
            self.accept_money('dime')
        if channel == self._pin_quarter:
            self.accept_money('quarter')

    def _get_product(self):
        while None == self._product:
            print(self._vm.get_products())
            self._product = input("Choice? ")
            self.check_purchase_state()


    def run(self):

        self._get_product()

        ch = ' '
        while ch != 'X':
            ch = input('X to exit')

            self._get_product()