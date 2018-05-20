from ..motor_controller import pwm_hat, motor
import RPi.GPIO as gpio

FRONT_RIGHT_MOTOR_PWM = 0
FRONT_RIGHT_MOTOR_DIR = 17

FRONT_LEFT_MOTOR_PWM = 1
FRONT_LEFT_MOTOR_DIR = 27

BACK_RIGHT_MOTOR_PWM = 2
BACK_RIGHT_MOTOR_DIR = 22

BACK_LEFT_MOTOR_PWM = 3
BACK_LEFT_MOTOR_DIR = 23


class MotorController:

    def __init__(self):

        self.pwm = pwm_hat.PwmHat(1000)

        self.front_left_motor = motor.Motor(FRONT_LEFT_MOTOR_PWM, FRONT_LEFT_MOTOR_DIR)
        self.front_right_motor = motor.Motor(FRONT_RIGHT_MOTOR_PWM, FRONT_RIGHT_MOTOR_DIR)

        self.back_left_motor = motor.Motor(BACK_LEFT_MOTOR_PWM, BACK_LEFT_MOTOR_DIR)
        self.back_right_motor = motor.Motor(BACK_RIGHT_MOTOR_PWM, BACK_RIGHT_MOTOR_DIR)

        gpio.setmode(gpio.BCM)

        gpio.setup(FRONT_RIGHT_MOTOR_DIR, gpio.OUT)
        gpio.setup(FRONT_LEFT_MOTOR_DIR, gpio.OUT)
        gpio.setup(BACK_RIGHT_MOTOR_DIR, gpio.OUT)
        gpio.setup(BACK_LEFT_MOTOR_DIR, gpio.OUT)

    def move(self, front_back, left_right):

        gpio.output(self.front_right_motor.direction_pin, gpio.HIGH)
        gpio.output(self.front_left_motor.direction_pin, gpio.HIGH)
        gpio.output(self.back_right_motor.direction_pin, gpio.HIGH)
        gpio.output(self.back_left_motor.direction_pin, gpio.HIGH)

        self.pwm.set_pwm(self.front_right_motor.pwm_pin, 2048)
        self.pwm.set_pwm(self.front_left_motor.pwm_pin, 2048)
        self.pwm.set_pwm(self.back_right_motor.pwm_pin, 2048)
        self.pwm.set_pwm(self.back_left_motor.pwm_pin, 2048)


