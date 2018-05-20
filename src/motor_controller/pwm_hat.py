import Adafruit_PCA9685


class PwmHat:

    # freq between 40 and 1000
    def __init__(self, freq=1000):
        self.pwm = Adafruit_PCA9685.PCA9685()
        self.pwm.set_pwm_freq(freq)
        self.freq = freq

    def set_pwm(self, channel, duty):
        self.pwm.set_pwm(channel, 0, duty)

    # Helper function to make setting a servo pulse width simpler.
    def set_servo_pulse(self, channel, pulse):
        pulse_length = 1000000  # 1,000,000 us per second
        pulse_length //= self.freq  # frequency
        print('{0}us per period'.format(pulse_length))
        pulse_length //= 4096  # 12 bits of resolution
        print('{0}us per bit'.format(pulse_length))
        pulse *= 1000
        pulse //= pulse_length
        self.pwm.set_pwm(channel, 0, pulse)

