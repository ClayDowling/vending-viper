#!/usr/bin/python3

import RPi.GPIO as GPIO

import physicalPanel

config = {
    'dispenser_pin': 26,
    'need_money_pin': 19,
    'nickel_pin': 6,
    'dime_pin': 5,
    'quarter_pin': 13
}


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

panel = physicalPanel.PhysicalPanel(config)
panel.run()