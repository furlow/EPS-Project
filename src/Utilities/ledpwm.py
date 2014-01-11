import RPi.GPIO as GPIO 
from time import sleep
LED_OUT_PIN = 13
GPIO.setmode(GPIO.BOARD) 
GPIO.setwarnings(False)
GPIO.setup(LED_OUT_PIN, GPIO.OUT, initial= GPIO.LOW)
light = GPIO.PWM(LED_OUT_PIN, 100)
light.start(0)
light.ChangeDutyCycle(1)
sleep(10)
