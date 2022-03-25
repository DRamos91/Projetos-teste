import requests as requests

import requests
import json
import classes

r = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
print(r)
print(r.json())

