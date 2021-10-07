import tkinter as tk
from tkinter import *
from pynput import mouse, keyboard
import time
import winsound
import threading

last_action_time = 0


def someFunc(max_time_between_actions, annoying_sound):
    global last_action_time
    last_action_time = time.time()
    while True:
        currentTime = time.time()
        if (currentTime - last_action_time > max_time_between_actions):
            if annoying_sound:
                winsound.PlaySound("screaming_sheep.wav", winsound.SND_ALIAS)
            else:
                winsound.Beep(3000, 1000)
        time.sleep(1)


def registerAction(*args):
    global last_action_time
    last_action_time = time.time()


keyboardListener = keyboard.Listener(
    on_press=registerAction,
    on_release=registerAction)

mouseListener = mouse.Listener(
    on_move=registerAction,
    on_click=registerAction,
    on_scroll=registerAction)


def startAlarm():
    # start process
    keyboardListener.start()
    mouseListener.start()
    timeDelay = int(alarmDelay.get())*60
    soundType = rbVariable.get()
    audioThread = threading.Thread(target=someFunc, args=(
        timeDelay, soundType,), daemon=True)
    audioThread.start()


def stopAlarm():
    # stop process
    keyboardListener.stop()
    mouseListener.stop()
    exit()


root = Tk()
root.iconbitmap(default='favicon.ico')
# this is the declaration of the variable associated with the radio button group
rbVariable = tk.IntVar()


# This is the section of code which creates the main window
root.geometry('280x120')
root.configure(background='#F0F8FF')
root.title('Get Productive')


# This is the section of code which creates the a label
Label(root, text='Alarm if idle for', bg='#F0F8FF',
      font=('arial', 12, 'normal')).place(x=20, y=10)


# This is the section of code which creates a text input box
alarmDelay = Entry(root)
alarmDelay.place(x=135, y=12, width=40)


# This is the section of code which creates the a label
Label(root, text='minutes', bg='#F0F8FF', font=(
    'arial', 12, 'normal')).place(x=185, y=10)


# This is the section of code which creates a group of radio buttons
frame = Frame(root, width=0, height=0, bg='#F0F8FF')
frame.place(x=20, y=40)
ARBEES = [
    ('Beep', '0'),
    ('Screaming Goat', '1'),
]
for text, mode in ARBEES:
    rbGroupOne = Radiobutton(frame, text=text, variable=rbVariable, value=mode, bg='#F0F8FF', font=(
        'arial', 12, 'normal')).pack(side='top', anchor='w')


# This is the section of code which creates a button
Button(root, text='Start', bg='#F0F8FF', font=('arial', 12, 'normal'),
       command=startAlarm).place(x=210, y=40)

Button(root, text='Stop', bg='#F0F8FF', font=('arial', 12, 'normal'),
       command=stopAlarm).place(x=210, y=80)


root.mainloop()
