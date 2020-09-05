## -SPSUL-

**Připojte PIR čidlo a přepínač. Přepínač aktivuje funkci PIR čidla (funkce zabezpečení objektu při odchodu). Při narušení zabezpečeného objektu rozsviťte červenou LED a spusťte alarm (bzučák). Chráněný prostor vymezte např. papírovými clonkami kolem PIR čidla.**

<br>

### Díly:
             - LED dioda
             - Tlačítko
             - Dráty 
             - Raspberry Pi 3 
             - Rezistor
             - Buzzer
             - PIR
     
    
<br>

### Kód

```
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO 
from time import sleep # Import sleep funkce z time modulu

GPIO.setwarnings(False) # Ignorování upozornění a varování
GPIO.setmode(GPIO.BOARD) # Použití fyzického pin číslování

pir_sensor = 29 #pir pin
buzzer = 32 #buzzer pin
i = 0 #toggle button state


GPIO.setup(37, GPIO.OUT) # pir led
GPIO.setup(31, GPIO.IN) #btn pir
GPIO.setup(buzzer,GPIO.OUT) #beeper
GPIO.setup(pir_sensor, GPIO.IN) #pir
current_state = 0 #pir state

while True:
    current_state = GPIO.input(pir_sensor)
    
    #urcuje toggle button state
    if GPIO.input(7) == GPIO.HIGH:
        if i == 0:
            i = 1
            print("ON")
        else:
            i = 0
            print("OFF")
        time.sleep(0.5)
    
    #pokud je toggled tak funguje pirko
    if i == 1:
        if current_state == 1:
            print("PIR ON")
            GPIO.output(32, GPIO.HIGH)
            GPIO.output(37, GPIO.HIGH)

        else:
            print("PIR OFF")
            GPIO.output(32, GPIO.LOW)
            GPIO.output(37, GPIO.LOW)
    
```



