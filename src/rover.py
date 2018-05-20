import time
from .motor_controller import motor_controller

if __name__ == '__main__':

    mc = motor_controller.MotorController()

    while True:
        mc.move(0, 0)
        time.sleep(1)




