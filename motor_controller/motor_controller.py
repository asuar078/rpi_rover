from motor_controller import pwm_hat, motor
import RPi.GPIO as gpio

FRONT_RIGHT_MOTOR_PWM = 0
FRONT_RIGHT_MOTOR_DIR = 22

FRONT_LEFT_MOTOR_PWM = 1
FRONT_LEFT_MOTOR_DIR = 17

BACK_RIGHT_MOTOR_PWM = 2
BACK_RIGHT_MOTOR_DIR = 18

BACK_LEFT_MOTOR_PWM = 3
BACK_LEFT_MOTOR_DIR = 27

PWM_FREQUENCY = 300
PWM_PRECISION = 4095
FORWARD = True
BACKWARD = False

# red, yellow, white, black

class MotorController:

    def __init__(self):
        print("creating motor controller")
        self.pwm = pwm_hat.PwmHat(PWM_FREQUENCY)

        self.front_left_motor = motor.Motor(FRONT_LEFT_MOTOR_PWM, FRONT_LEFT_MOTOR_DIR)
        self.front_right_motor = motor.Motor(FRONT_RIGHT_MOTOR_PWM, FRONT_RIGHT_MOTOR_DIR)

        self.back_left_motor = motor.Motor(BACK_LEFT_MOTOR_PWM, BACK_LEFT_MOTOR_DIR)
        self.back_right_motor = motor.Motor(BACK_RIGHT_MOTOR_PWM, BACK_RIGHT_MOTOR_DIR)

        gpio.setmode(gpio.BCM)

        gpio.setup(FRONT_RIGHT_MOTOR_DIR, gpio.OUT)
        gpio.setup(FRONT_LEFT_MOTOR_DIR, gpio.OUT)
        gpio.setup(BACK_RIGHT_MOTOR_DIR, gpio.OUT)
        gpio.setup(BACK_LEFT_MOTOR_DIR, gpio.OUT)

    def __del__(self):
        print("closing motor controller")
        self.pwm.turn_all_off()
        gpio.cleanup()

    def left_motors(self, angle, strength):
        duty_cycle = int(PWM_PRECISION*strength/100.0)
        print("left duty cycle: " + str(duty_cycle))
        if 0 <= angle <= 180:
            self.front_left(forward=True, duty=duty_cycle)
            self.back_left(forward=True, duty=duty_cycle)
        else:
            self.front_left(forward=False, duty=duty_cycle)
            self.back_left(forward=False, duty=duty_cycle)

    def right_motors(self, angle, strength):
        duty_cycle = int(PWM_PRECISION*strength/100.0)
        if 0 <= angle <= 180:
            self.front_right(forward=True, duty=duty_cycle)
            self.back_right(forward=True, duty=duty_cycle)
        else:
            self.front_right(forward=False, duty=duty_cycle)
            self.back_right(forward=False, duty=duty_cycle)

    def front_right(self, forward=True, duty=2048):
        if forward:
            gpio.output(self.front_right_motor.direction_pin, gpio.HIGH)
        else:
            gpio.output(self.front_right_motor.direction_pin, gpio.LOW)

        self.pwm.set_pwm(self.front_right_motor.pwm_pin, duty)

    def front_left(self, forward=True, duty=2048):
        if forward:
            gpio.output(self.front_left_motor.direction_pin, gpio.HIGH)
        else:
            gpio.output(self.front_left_motor.direction_pin, gpio.LOW)

        self.pwm.set_pwm(self.front_left_motor.pwm_pin, duty)

    def back_right(self, forward=True, duty=2048):
        if forward:
            gpio.output(self.back_right_motor.direction_pin, gpio.LOW)
        else:
            gpio.output(self.back_right_motor.direction_pin, gpio.HIGH)

        self.pwm.set_pwm(self.back_right_motor.pwm_pin, duty)

    def back_left(self, forward=True, duty=2048):
        if forward:
            gpio.output(self.back_left_motor.direction_pin, gpio.LOW)
        else:
            gpio.output(self.back_left_motor.direction_pin, gpio.HIGH)

        self.pwm.set_pwm(self.back_left_motor.pwm_pin, duty)

    def forward(self, duty=0.5):
        output = int(PWM_PRECISION * duty)

        self.front_right(FORWARD, output)
        self.front_left(FORWARD, output)
        self.back_right(FORWARD, output)
        self.back_left(FORWARD, output)

    def backwards(self, duty=0.5):
        output = int(PWM_PRECISION * duty)

        self.front_right(BACKWARD, output)
        self.front_left(BACKWARD, output)
        self.back_right(BACKWARD, output)
        self.back_left(BACKWARD, output)

    def turn_left(self, duty=0.5):
        output = int(PWM_PRECISION * duty)

        self.front_right(FORWARD, output)
        self.front_left(BACKWARD, output)
        self.back_right(FORWARD, output)
        self.back_left(BACKWARD, output)

    def turn_right(self, duty=0.5):
        output = int(PWM_PRECISION * duty)

        self.front_right(BACKWARD, output)
        self.front_left(FORWARD, output)
        self.back_right(BACKWARD, output)
        self.back_left(FORWARD, output)
