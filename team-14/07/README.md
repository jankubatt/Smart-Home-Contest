# NAG-IoT
## -SPSUL-

**Připojte čtečku karet a čipů (RFID-RC522). Naprogramujte čtení vybraných karet a čipů. Pro vybranou skupinu otvírejte závoru, na ostatní karty reagujte rozsvícením červené LED.**

<br>

### Díly:
             - LED dioda
             - RC522
             - Dráty 
             - Raspberry Pi 3 
             - Rezistor
             - RFID Tag
     
    
<br>

### Kód

```
#Import knihoven
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep


reader = SimpleMFRC522() #rc522
ObstaclePin = 26 #rc522 pin

#GPIO Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(ObstaclePin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#pwm setup
pwm=GPIO.PWM(11, 50)
pwm.start(0)


#Nastaveni uhlu
def SetAngle(angle):
    duty = angle / 18 + 3
    GPIO.output(11, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(11, False)
    pwm.ChangeDutyCycle(0)

while True:
    print(GPIO.input(ObstaclePin))
    id, text = reader.read() #id a text precteneho cipu
    print(id)
    print(text)
    
    if id == 408013704495: #pokud cislo tagu == 408013704495, tak otevre zavoru
        SetAngle(170)
        sleep(10)
        while (0 == GPIO.input(ObstaclePin)):
            sleep(3)
        SetAngle(100)
```



