import requests
import time 

url = "http://192.168.1.115"

while 1:
    response = requests.get(url)
    print("Data received from Arduino:", response.text)
