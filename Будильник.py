from tkinter import *
from time import strftime
from tkinter import messagebox
import pygame as pg

"""Лекция"""

def tick():
    global time_run
    current_time = strftime('%H:%M:%S')
    current_time1 = strftime('%H:%M')
    current_time2 = strftime('%H')
    text.config(text=current_time)
    if (time_run == current_time or time_run == current_time1
            or time_run == current_time2):
        time_run = ''
        pg.mixer.music.play()
    text.after(1000, tick)

def on():
    global time_run
    time_run = entry.get().strip()
    text.config(text=time_run)
    messagebox.showinfo('Время  установки будильника',
                        f'Будильник установлен на {time_run}')


def off():
    global time_run
    time_run = ''
    pg.mixer.music.stop()
    messagebox.showwarning('Предупреждение',
                           f'Будильник выключен')



pg.mixer.init()
pg.mixer.music.load('music.mp3')
time_run = ''
root = Tk()
root.config(bg="black")
# root.geometry("400x250+200+200") # смещение по x, y
WIDTH = root.winfo_screenwidth()
Height = root.winfo_screenheight()
X = 400
Y = 250
root.geometry(f"{X}x{Y}+{WIDTH // 2 - X // 2}"
              f"+{Height // 2 - Y // 2 - 20}")
root.title("Alarm")

text = Label(root, text="00:00:00")
text.config(font=("Arial", 50), fg="lime", bg="black")
text.pack(side=TOP)

entry = Entry(root, font=("Arial", 20), fg="white", width=20, justify=CENTER)
entry.pack(pady=10)
entry.focus_set()



btn = Button(text='Set', width=10, command=on)
btn.pack(pady=5)

btn1 = Button(text='Turn off', width=10, command=off)
btn1.pack(pady=5)

tick()

root.mainloop()

