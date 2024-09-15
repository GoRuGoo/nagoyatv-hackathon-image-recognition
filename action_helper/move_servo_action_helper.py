import pigpio
import time


class MoveServoActionHelper:
    def __init__(self, pin):
        self.pin = pin
        self.pi = pigpio.pi()
        self.pi.set_mode(self.pin, pigpio.OUTPUT)

    def forward(self):
        self.pi.set_servo_pulsewidth(self.pin, 1000)

    def reverse(self):
        self.pi.set_servo_pulsewidth(self.pin, 2000)

    def stop(self):
        self.pi.set_servo_pulsewidth(self.pin, 1500)

    def cleanup(self):
        self.pi.set_servo_pulsewidth(self.pin, 0)
        self.pi.stop()
