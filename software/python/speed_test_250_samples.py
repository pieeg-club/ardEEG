import socket
from scipy import signal
import csv
from datetime import datetime
import sys
import time

UDP_IP = "192.168.1.241"    # your wifi IP   
UDP_PORT = 13900            # your free port 

data_lenght = 1350  #   6,750
per_sec =  6750

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print ("ok1")
sock.bind((UDP_IP, UDP_PORT))
result = data_lenght*[0]
count_value = 0

start_time = time.time()
while True:
    data, addr = sock.recvfrom(data_lenght)  
    count_value = count_value+1
        
    if count_value == 25:
        print("--- %s seconds ---" % (time.time() - start_time))
        await_receive = count_value*(data_lenght/per_sec)
        print ("expected", await_receive)
        sys.exit()
