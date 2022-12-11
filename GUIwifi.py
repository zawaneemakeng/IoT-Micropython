from tkinter import *
import socket
import threading


def runserver():
    serverip = '192.168.1.97'
    port = 9000

    buffsize = 4096

    while True:
        server = socket.socket()
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((serverip, port))
        server.listen(1)
        print('waiting micropython...')

        client, addr = server.accept()
        print('connected from:', addr)

        data = client.recv(buffsize).decode('utf-8')
        print('Data from MicroPython: ', data)
        # data = 'LED1 : ON'/'LED2: OFF'
        data_split = data.split(':')
        if data_split[1] == 'ON':
            v_status.set('{} สถานะ {} '.format(data_split[0], data_split[1]))
            L2.configure(fg='#4ec248')

        else:
            v_status.set('{} สถานะ {} '.format(data_split[0], data_split[1]))
            L2.configure(fg='#e83333')

        client.send('received your messages.'.encode('utf-8'))
        client.close()


GUI = Tk()
GUI.title("IoT Status by zawanee")
GUI.geometry('700x500')
FONT = ('Angsana New', 30)

# ข้อความไม่เปลี่ยนเเปลง
L1 = Label(GUI, text='LED Status from Micropython', font=FONT,)
L1.pack()

# ข้อความเปลี่ยนเเปลง
v_status = StringVar()
v_status.set('<<<<<<< NO Status >>>>>>>>>')

L2 = Label(GUI, textvariable=v_status, font=FONT, )
L2.configure(fg='#8539a8')
L2.pack()


#########runserver###########
task = threading.Thread(target=runserver)
task.start()
GUI.mainloop()
