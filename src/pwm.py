import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

my_pwm=GPIO.PWM(17,100)

my_other=GPIO.PWM(4,100)

my_pwm.start(0)
my_other.start(0)

while(1):
    fast=input("How fast? (20-100)")
    if fast == 101:
        break
    
    my_pwm.ChangeDutyCycle(fast)
    my_other.ChangeDutyCycle(fast)

print "exiting loop"
my_pwm.stop()
GPIO.cleanup()
