import RPi.GPIO as GPIO
import time


class ToggleSwitchStateProvider:
    def __init__(self, pin):
        GPIO.setmode(GPIO.BCM)
        self.pin = pin
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def get_state(self):
        return GPIO.input(self.pin)

    def __del__(self):
        GPIO.cleanup()
