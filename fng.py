
from machine import PWM, Pin

class Fng:
    def __init__(self, pwm_pin, cw_pin, ccw_pin):
        self.pwm_pin = pwm_pin
        self.cw_pin = Pin(cw_pin, Pin.OUT)
        self.ccw_pin = Pin(ccw_pin, Pin.OUT)

        self.motor = PWM(Pin(self.pwm_pin), freq=1000, duty=0)
        #begin.freq(1000) # Set PWM frequency 1000Hz
        #begin.duty(0)

    def write(self, pwm_in, dir):
        if dir == 'ccw':
            self.ccw_pin.on()
        else:
            self.cw_pin.on()
        self.motor.duty(pwm_in)

        