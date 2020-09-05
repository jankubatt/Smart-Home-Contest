# NAG-IoT
## -SPSUL-

**Doplňte závoru o infra čidlo a naprogramujte ovládání závory tak, aby v případě, že v prostoru závory je překážka, závora zůstane zdvižená a spustí se až po odstranění překážky.**

<br>

### Díly:
             - 9g Servo
             - Tlačítko
             - Dráty 
             - Raspberry Pi 3 
             - 220 Ohm rezistor
             - IR SENSOR OBSTACLE AVOIDANCE SENSOR
     
     
    
<br>

### Kód

```
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO
from time import sleep # Import sleep funkce z time modulu

GPIO.setwarnings(False) # Ignorování upozornění a varování
GPIO.setmode(GPIO.BOARD) # Použití fyzického pin číslování
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) # IR Detektor překážek
GPIO.setup(11, GPIO.OUT) # servo
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # tlačítko

pwm=GPIO.PWM(11, 50) # nastavení PWM
pwm.start(0) # start PWM

# nastavení úhlu
def SetAngle(angle):
    duty = angle / 18 + 3
    GPIO.output(11, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(11, False)
    pwm.ChangeDutyCycle(0)
 
while True:
    if GPIO.input(13) == GPIO.HIGH: # pokud se zmáčkne tlačítko, závora se otevře na 10 sekund. Poté kontroluje, zda li není překážka v oblasti závory, pokud ano přidá sekundu navíc
        print("Zavora")
        
        SetAngle(170)
        sleep(10)
        
        while (0 == GPIO.input(24)):
            sleep(1)
        
        SetAngle(100)
```





