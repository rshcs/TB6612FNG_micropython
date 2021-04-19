
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
        if dir == 'cw':
            self.cw_pin.off() # Turns on cw_pin
            self.ccw_pin.on() # Some nodemcu's wires connected in other way around 
        elif dir == 'ccw':
            self.cw_pin.on()
            self.ccw_pin.off()
        self.motor.duty(pwm_in)

if __name__ == '__main__':
    m1 = Fng(14, 0, 2)
    m2 = Fng(12, 13, 15)

    m1.write(0, 'cw')
    m2.write(0, 'cw')