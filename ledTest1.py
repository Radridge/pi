import RPi.GPIO as GPIO
import time

LED_LIST = [17, 27, 22]
BUTTON = 26

GPIO.setmode(GPIO.BCM)
for lit in LED_LIST:
    GPIO.setup(lit, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN)

while True:
    bVal = GPIO.input(BUTTON)
    time.sleep(0.1)
    if bVal == 1:
        for lits in LED_LIST:
            GPIO.output(lits, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(lits, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(lits, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(lits, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(lits, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(lits, GPIO.LOW)

GPIO.cleanup()