import RPi.GPIO as GPIO 

GPIO.setmode(GPIO.BOARD) 
GPIO.setwarnings(False)
GPIO.setup(13, GPIO.OUT, initial= GPIO.LOW)
