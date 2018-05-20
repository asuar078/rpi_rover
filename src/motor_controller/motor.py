
class Motor:

    pwm_pin = 0
    direction_pin = 0
    current_pin = 0
    enc_a_pin = 0
    enc_b_pin = 0

    def __init__(self, pwm_pin, direction_pin, current_pin=0, enc_a_pin=0, enc_b_pin=0):
        self.pwm_pin = pwm_pin
        self.direction_pin = direction_pin
        self.current_pin = current_pin
        self.enc_a_pin = enc_a_pin
        self.enc_b_pin = enc_b_pin


