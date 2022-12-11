import time
from threading import Thread
from tkinter import *
from PIL import Image, ImageTk

GUI = Tk()
GUI.geometry('1000x900')
GUI.title('Dashboard IoT Smart Farm')
GUI.state('zoomed')  # full screen

# CANVAS กระดาณวาดภาพ
canvas = Canvas(GUI, width=1500, height=900)
canvas.place(x=0, y=0)

background = ImageTk.PhotoImage(Image.open('farm.png'))
canvas.create_image(400, 150, anchor=NW, image=background)

#####################DDOR#####################
# วาดสี่เหลี่ยม
canvas.create_polygon([731, 378, 775, 404, 775, 444, 731, 419],
                      fill='green', outline=None, tags='d1')
canvas.create_text(300, 300, text='ประตูฟาร์มกำลังเปิด',
                   fill='green', font=('Ansana New', 30), tags='d1')

canvas.create_line(452, 306, 732, 405,
                   fill='gray', width=3)
door_state = TRUE


def DoorOnOff(event):
    global door_state  # การเปลียนตัวเเปรด้านนอกฟังชั่น
    door_state = not door_state  # สลับสถานะ
    canvas.delete('d1')  # delete
    if door_state == TRUE:
        canvas.create_polygon([731, 378, 775, 404, 775, 444, 731,
                               419], fill='green', outline=None, tags='d1')
        canvas.create_text(300, 300, text='ประตูฟาร์มกำลังเปิด',
                           fill='green', font=('Ansana New', 30), tags='d1')
        canvas.create_line(452, 306, 732, 405,
                           fill='gray', width=3)
    else:
        canvas.create_polygon([731, 378, 775, 404, 775, 444, 731,
                               419], fill='red', outline=None, tags='d1')
        canvas.create_text(300, 300, text='ประตูฟาร์มกำลังปิด',
                           fill='red', font=('Ansana New', 30), tags='d1')
        canvas.create_line(452, 306, 732, 405,
                           fill='gray', width=3)


fan = ImageTk.PhotoImage(Image.open('fan.png'))
canvas.create_image(200, 200, image=fan, tags='img3', anchor='center')


angle = 0


def run_fan(event=None):
    # fan = ImageTk.PhotoImage(resize_image('fan-icon.png',100))
    global angle
    while True:
        if angle != 0:
            canvas.delete('img3')
            fan = ImageTk.PhotoImage(image=Image.open('fan.png').rotate(angle))
            canvas.create_image(1173, 408, image=fan, tags='img3')
        angle += 20
        if angle >= 360:
            angle = 0
        time.sleep(0.1)


task = Thread(target=run_fan)
task.start()

GUI.bind('<Return>', DoorOnOff)


GUI.mainloop()
