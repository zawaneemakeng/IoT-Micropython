import socket
import network
import time
from machine import Pin
import dht

#####################
serverip = '192.168.1.73'
port = 9000
#####################
wifi = 'wifi name'
password = 'password'
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
time.sleep(2)
wlan.connect(wifi, password)
time.sleep(2)
print(wlan.isconnected())
time.sleep(1)


def send_data(data):
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.connect((serverip, port))
    server.send(data.encode('utf-8'))
    data_server = server.recv(1024).decode('utf-8')
    print('Server:', data_server)
    server.close()


print('Temperature checking...')
d = dht.DHT22(Pin(23))


for i in range(20):
    d.measure()
    temp = d.temperature()
    humid = d.humidity()
    print(temp)
    print('{:.2f}'.format(humid))
    print('----------')
    text = 'TEMP:{}'.format(temp)
    send_data(text)
    time.sleep(3)
