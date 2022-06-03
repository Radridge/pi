import RPi.GPIO as GPIO
import time

LED_UNO = 17
LED_DOS = 27
LED_TRES = 22
BUTTON_UNO = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_UNO, GPIO.OUT)
GPIO.setup(LED_DOS, GPIO.OUT)
GPIO.setup(LED_TRES, GPIO.OUT)
GPIO.setup(BUTTON_UNO, GPIO.IN)

while True:
    bVal = GPIO.input(BUTTON_UNO)
    time.sleep(0.1)
    if bVal == 1:
        GPIO.output(LED_UNO, GPIO.HIGH)
        GPIO.output(LED_DOS, GPIO.LOW)
        GPIO.output(LED_TRES, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED_UNO, GPIO.LOW)
        GPIO.output(LED_DOS, GPIO.HIGH)
        GPIO.output(LED_TRES, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(LED_UNO, GPIO.HIGH)
        GPIO.output(LED_DOS, GPIO.LOW)
        GPIO.output(LED_TRES, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED_UNO, GPIO.LOW)
        GPIO.output(LED_DOS, GPIO.HIGH)
        GPIO.output(LED_TRES, GPIO.LOW)

GPIO.cleanup()