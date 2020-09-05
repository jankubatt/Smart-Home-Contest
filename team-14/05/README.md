# NAG-IoT
## -SPSUL-

**Sestavte příjezdovou závoru, pohon závory je servo. Závora se zdvíhá při stisku tlačítka a spustí se automaticky po 10 sekundách.**

<br>

### Díly:
          - 9g Servo
          - Dráty
          - Tlačítko
          - Raspberry Pi 3
          - Závora
          - 220 Ohm rezistor

<br>

### Kód

```
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO 
from time import sleep # Import sleep funkce z time modulu

GPIO.setwarnings(False) # Ignorování upozornění a varování
GPIO.setmode(GPIO.BOARD) # Použití fyzického pin číslování

GPIO.setup(11, GPIO.OUT) #servo
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #button

pwm=GPIO.PWM(11, 50) #nastavení pwm
pwm.start(0) #pwm start

#nastavení úhlu
def SetAngle(angle):
    duty = angle / 18 + 3
    GPIO.output(11, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(11, False)
    pwm.ChangeDutyCycle(0)
    
while True:
    if GPIO.input(10) == GPIO.HIGH: # pokud se zmáčkne tlačítko, tak se závora zvedne (170 stupňů) počká 10 sekund a pak klesne (100 stupňů)
        SetAngle(170)
        sleep(10)
        SetAngle(100)
    
```