import RPi.GPIO as GPIO
import time

LED_LIST = [17, 27, 22]
BUTTON = 26

def singleLightOn(lightNumber):
    for pin in LED_LIST:
        if pin == lightNumber:
            GPIO.output(pin, GPIO.HIGH)
        else:
            GPIO.output(pin, GPIO.LOW)

GPIO.setmode(GPIO.BCM)
for lit in LED_LIST:
    GPIO.setup(lit, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN)

prevBVal = GPIO.input(BUTTON)
ledIndex = 0
while True:
    time.sleep(0.1)
    bVal = GPIO.input(BUTTON)
    if bVal != prevBVal:
        prevBVal = bVal
        if bVal == GPIO.HIGH:
            singleLightOn(LED_LIST[ledIndex])
            ledIndex += 1
            if ledIndex >= len(LED_LIST):
                ledIndex = 0 
