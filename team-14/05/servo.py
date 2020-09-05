import RPi.GPIO as GPIO #GPIO library
from time import sleep #time library
GPIO.setmode(GPIO.BOARD) #pin číslování
GPIO.setwarnings(False) #varování off
GPIO.setup(11, GPIO.OUT) #servo
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #button
GPIO.setup(33, GPIO.OUT, initial=GPIO.LOW) #led na sloupku serva

pwm=GPIO.PWM(11, 50)
pwm.start(0)

#funkce pro úhel závory
def SetAngle(angle):
    duty = angle / 18 + 3
    GPIO.output(11, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(11, False)
    pwm.ChangeDutyCycle(0)
    
while True:
	if GPIO.input(13) == GPIO.HIGH:
        GPIO.output(33, GPIO.HIGH)
		SetAngle(170)
        sleep(10)
		SetAngle(100)
        GPIO.output(33, GPIO.LOW)