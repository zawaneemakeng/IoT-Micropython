import socket
import network
import time
from machine import Pin

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


def send_data(data):
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.connect((serverip, port))
    server.send(data.encode('utf-8'))
    data_server = server.recv(1024).decode('utf-8')
    print('Server:', data_server)
    server.close()


led = Pin(23, Pin.OUT)

while True:
    led.on()
    send_data('LED:ON')
    time.sleep(3)
    led.off()
    send_data('LED:OFF')
    time.sleep(3)
