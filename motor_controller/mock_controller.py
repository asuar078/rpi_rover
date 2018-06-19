
class MockController:

    def __init__(self):
        print("creating mock controller")

    def __del__(self):
        print("closing mock controller")

    def left_motors(self, angle, strength):
        print("moving left motor: " + str(angle) + ":" + str(strength))

    def right_motors(self, angle, strength):
        print("moving right motor: " + str(angle) + ":" + str(strength))
