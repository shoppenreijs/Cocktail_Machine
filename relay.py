import RPi.GPIO as GPIO
import time

motor1 = 21
motor2 = 20
motor3 = 16
motor4 = 26

motor_list = [motor1, motor2, motor3, motor4]
# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(motor_list, GPIO.OUT)


def motor_on(pin):
    GPIO.output(pin, GPIO.HIGH)  # Turn motor on


def motor_off(pin):
    GPIO.output(pin, GPIO.LOW)  # Turn motor off


try:
    motor_on(motor1)
    time.sleep(2)
    motor_off(motor1)
    time.sleep(2)
    motor_on(motor2)
    time.sleep(1)
    motor_off(motor2)
    time.sleep(1)
    GPIO.cleanup()
except KeyboardInterrupt:
    GPIO.cleanup()
