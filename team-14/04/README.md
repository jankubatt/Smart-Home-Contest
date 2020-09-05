# NAG-IoT
## -SPSUL-

**Aktuální hodnotu osvětlení posílejte v pravidelných intervalech na soutěžní server.**

<br>

### Postup
Pro odesílání dat na server jsem se rozhodl použít RPi 3 s knihovnou requests v pythonu. Data odesílám na API.
```
import requests

url = 'https://api.nag-iot.zcu.cz/v2/value/PROMENNA?api_key=API_KLIC'
myobj = {'value': HODNOTA_SENZORU}

x = requests.post(url, json = myobj)

print(x.status_code)
print(x.text)
```
            
### Kód
- u třetího úkolu