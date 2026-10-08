# import tkinter as tk # я импортирую библиотеку ткинтер как тк
# from dataclasses import replace
# from fileinput import close
from tkinter import *
import random
# import tkinterweb
from tkinter import messagebox as mb

from tkinter.constants import BOTTOM


# если убрать as tk, библиотека все равно будет работать


# def replace():
#     label.config(text='NOOOOOOOOOOOO')
#
#
# def decrease():
#     number.set(number.get() - 5)
#
#
# def increase():
#     number.set(number.get() + 5)
#
# def print_entry():
#    print(entry.get())
#
#
# win = tk.Tk()
# win.geometry('600x400')
# win.title('Ксюша vs Python')
#
# number = tk.IntVar(value=0)
#
# fr_center = tk.Frame(win)
# fr_center.pack()
#
# fr2 = tk.Frame(fr_center)
# fr2.pack(side='left')
#
# fr3 = tk.Frame(fr_center)
# fr3.pack(side='right')
#
#
# label = tk.Label(fr3, textvariable = number, bg = 'lightblue', fg = "blue", font = ('Arial', 14), height = 3, width = 20)
# label.pack(pady = 10)
#
# button1 = tk.Button(fr2, text = 'Дай 5', command=increase)
# button1.pack(pady = 10)
#
# button2 = tk.Button(fr2, text = 'Возьми 5', command=decrease)
# button2.pack(pady = 10)
#
# entry = tk.Entry(fr3, width=40)
# entry.pack(pady = 10)
#
# button3 = tk.Button(fr2, text = 'Иди в консоль!', command=print_entry)
# button3.pack(pady = 10)
#
# tk.mainloop()

# """Лекция"""
#
#
# def res(event=None):
#     item = entry.get().strip()
#     try:
#         item = int(item) + 100
#     except ValueError:
#         item = 'Empty'
#     result.config(text=item)
#
#
# root = Tk()
# # root.geometry("400x250+200+200") # смещение по x, y
# WIDTH = root.winfo_screenwidth()
# Height = root.winfo_screenheight()
# X = 400
# Y = 250
# root.geometry(f"{X}x{Y}+{WIDTH // 2 - X // 2}"
#               f"+{Height // 2 - Y // 2 - 20}")
# root.title("Let's try")
#
# text = Label(root, text="Enter the number:")
# text.config(font=("Arial", 20), fg="white", bg="grey")
# text.pack(side=TOP)
#
# entry = Entry(root, font=("Arial", 20), fg="white", width=20, justify=CENTER)
# entry.pack(pady=10)
# entry.focus_set()
# result = Label(root, text="  "*10, bg='grey', font=("Arial", 20))
# result.config(justify=CENTER)
# result.pack(pady=10)
#
# btn = Button(text='Push', command=res)
# btn.pack(pady=10)
#
# entry.bind("<Return>", res)
#
# root.mainloop()

"""Семинар"""

# window = Tk()
# frame = tkinterweb.HtmlFrame(window)
# frame.load_website('http://www.google.com')
# frame.pack(fill="both",expand=1)
# window.mainloop()

# import tkinterweb
# from tkinter import *
#
# def read():
#     Site = e.get().strip()
#     if Site:
#         frame.load_url('https://' + Site)
#
# window = Tk()
# m = Label(text="Введите адрес сайта:")
# m.pack()
#
# e = Entry(width=20, justify='left')
# e.pack()
#
# b = Button(text="Ввод", command=read)
# b.pack()
#
# # insecure_https=True — отключает проверку SSL-сертификатов
# frame = tkinterweb.HtmlFrame(window, insecure_https=True)
# frame.pack(fill="both", expand=1)
#
# window.mainloop()

# Выводим только дату

# from tkinter import *
#
# import time
# window=Tk()
# window.title('Calendar')
# window.geometry('600x200')
# Month = time.strftime('%B')
# Year = time.strftime('%Y')
# match Month:
#     case 'January':
#         Month = 'Январь'
#     case 'February':
#         Month = "Февраль"
#     case 'March':
#         Month ="Март"
#     case 'April':
#         Month = "Апрель"
#     case 'May':
#         Month = "Май"
#     case 'June':
#         Month = "Июнь"
#     case 'July':
#         Month = "Июль"
#     case 'August':
#         Month = "Август"
#     case 'September':
#         Month = "Сентябрь"
#     case 'October':
#         Month = "Октябрь"
#     case 'November':
#         Month = "Ноябрь"
#     case 'December':
#         Month = "Декабрь"
# m = Label(font="Verdana 24 bold")
# m.pack()
# m.config(text=Month + " " + Year)
# window.mainloop()


# def night():
#     m.config(bg="black", fg="white")
#     R1.config(bg="black", fg="white")
#     R2.config(bg="black", fg="white")
#     R3.config(bg="black", fg="white")
#     R4.config(bg="black", fg="white")

# Задача 22: Создаем анкету

# def close():
#     window.destroy()
#
# def clear():
#     name_entry.delete(0, END)
#     surname_entry.delete(0, END)
#     petname_entry.delete(0, END)
#     age_entry.delete(0, END)
#     txt.delete('1.0', END)
#     result_l.config(text='')
#
#
#
# def info():
#     name = name_entry.get()
#     surname = surname_entry.get()
#     petname = petname_entry.get()
#     age = age_entry.get()
#     about = txt.get('1.0', END)
#     # if name == '' or surname == '' or petname == '' or age == '':
#         # result_l.config(text='Error: Required fields are not filled')
#     if not name or not surname or not petname or not age:
#         messagebox.showwarning('Warning', 'Required fields are not filled')
#         return
#     if not age.isdigit():
#         messagebox.showwarning('Warning', 'Age must be number')
#         return
#
#     result_l.config(text=(f'Now I know everything about you, {name} {surname}. \nYou are {age} years old! As you say, {about}\nAnd I am coming for {petname}'))
#     # messagebox.showinfo('I know everything about you!',
#     #                     f'Name: {name}\nSurname: {surname}\nPetname: {petname}\nAge: {age}')
#
#
# window=Tk()
# window.geometry('600x500')
# window.title('Секретная анкета')
#
# header_frame = Frame(window)
# header_frame.pack()
#
# form_frame = Frame(window)
# form_frame.pack()
#
# text_frame = Frame(window)
# text_frame.pack()
#
# button_frame = Frame(window)
# button_frame.pack()
#
# l=Label(header_frame, text='Tell me about you')
# l.pack()
#
# name_l=Label(form_frame, text='Name')
# name_l.grid(row=0, column=0)
#
# name_entry=Entry(form_frame)
# name_entry.grid(row=0, column=1)
#
# surname_l=Label(form_frame, text='Surname')
# surname_l.grid(row=1, column=0)
#
# surname_entry=Entry(form_frame)
# surname_entry.grid(row=1, column=1)
#
# petname_l=Label(form_frame, text='Petname')
# petname_l.grid(row=2, column=0)
#
# petname_entry=Entry(form_frame)
# petname_entry.grid(row=2, column=1)
#
# age_l=Label(form_frame, text='Age')
# age_l.grid(row=3, column=0)
#
# age_entry=Entry(form_frame)
# age_entry.grid(row=3, column=1)
#
# gender = StringVar()
#
# R1 = Radiobutton(form_frame, variable=gender, value="male", text="Male")
# R1.grid(row = 4,column = 0)
#
# R2 = Radiobutton(form_frame, variable=gender, value="female", text="Female")
# R2.grid(row = 4,column = 1)
#
# about_l = Label(text_frame, text='About me')
# about_l.pack()
#
# txt = Text(text_frame, width=40, height=8)
# txt.pack(side=LEFT)
#
# scrollbar = Scrollbar(text_frame, command=txt.yview)
# scrollbar.pack(side=RIGHT, fill=Y)
# txt.config(yscrollcommand=scrollbar.set)
#
# btn_info = Button(button_frame, text="Show info", command=info)
# btn_info.pack(pady=3)
#
# btn_close = Button(button_frame, text='Close', command=close)
# btn_close.pack(pady=3)
#
# btn_clear = Button(button_frame, text='Clear', command=clear)
# btn_clear.pack(pady=3)
#
# result_l=Label(button_frame, text='')
# result_l.pack()


#
# drink = StringVar(value=coffee)
# m = Label(text="Выбери любимый напиток:")
# m.pack()
#
# R1 = Radiobutton(text=kvas, value=kvas, variable=drink)
# R1.pack()
#
# R2 = Radiobutton(text=tea, value=tea, variable=drink)
# R2.pack()
#
# R3 = Radiobutton(text=coffee, value=coffee, variable=drink)
# R3.pack()
#
# m2 = Label(textvariable=drink)
# m2.pack()

# window.mainloop()


# def play():
#     computer = random.choice(["red", "yellow", "green"])
#     your_choice = light.get()
#     if your_choice == computer:
#         result_l.config(text='You win!')
#     else:
#         result_l.config(text=(f'You lose! I chose {computer}\n Once more?'))
#
# window=Tk()
# window.geometry('300x200')
# window.title('Traffic light')
#
# # red = "red"
# # green = "green"
# # yellow = "yellow"
#
# light = StringVar(value="red")
# # drink = StringVar(value=coffee)
# l=Label(window, text='Choose color')
# l.pack()
#
# R1 = Radiobutton(window, text="red", value="red", variable=light)
# R1.pack()
#
# R2 = Radiobutton(window, text="yellow", value="yellow", variable=light)
# R2.pack()
#
# R3 = Radiobutton(window, text="green", value="green", variable=light)
# R3.pack()
#
# btn_choose = Button(window, text='Choose', command=play)
# btn_choose.pack(pady=3)
#
# result_l=Label(window, text='')
# result_l.pack()
# window.mainloop()
# Окна Messagebox
# Окно askyesno
# import messagebox as mb
def check():
    answer = mb.askyesno(title="Вопрос", message="Перенести данные?")
    if answer:
        s = e.get()
        e.delete(0, END)
        m['text'] = s

window = Tk()
e = Entry()
e.pack()
b = Button(text="Передать", command=check)
b.pack()
m = Label(height=3)
m.pack()
window.mainloop()


