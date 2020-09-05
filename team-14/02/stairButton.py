import RPi.GPIO as GPIO #GPIO library
from time import sleep #time library

GPIO.setwarnings(False) #varování off
GPIO.setmode(GPIO.BOARD) #pin číslování
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW) #led 
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #button

while True:
    if GPIO.input(7) == GPIO.HIGH:
        GPIO.output(12, GPIO.HIGH)
        sleep(10)
        GPIO.output(12, GPIO.LOW)
        
    else:
        GPIO.output(12, GPIO.LOW)