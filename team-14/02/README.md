## -SPSUL-

**Připojte LED jako vnitřní osvětlení domu a ovládací tlačítko. Tlačítko naprogramujte jako schodišťový spínač, tj. po stisknutí svítí LED 10 sekund a pak sama zhasne.**

<br>

### Díly:
             - LED dioda
             - Tlačítko
             - Dráty 
             - Raspberry Pi 3 
             - Rezistor
     
![02](https://git.nag-iot.zcu.cz/NAG-IoT/tym-14/raw/branch/master/02/ukol02.png)
    
<br>

### Kód

```
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO 
from time import sleep # Import sleep funkce z time modulu

GPIO.setwarnings(False) # Ignorování upozornění a varování
GPIO.setmode(GPIO.BOARD) # Použití fyzického pin číslování
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # LED pin na začátku LOW
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # tlačítko

while True:
    if GPIO.input(10) == GPIO.HIGH: # pokud se zmáčkne tlačítko, tak se ledka rozsvítí na 10 sekund
        GPIO.output(8, GPIO.HIGH) # LED on
        sleep(10) # počkej 10 sekund
        GPIO.output(8, GPIO.LOW) # LED off
        
    else:
        GPIO.output(8, GPIO.LOW) # LED off
```



