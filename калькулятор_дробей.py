from tkinter import *
import math


def add (n1, d1, n2, d2):
    n = n1 * d2 + n2 * d1
    d = d1 * d2
    return n, d


def sub (n1, d1, n2, d2):
    n = n1 * d2 - n2 * d1
    d = d1 * d2
    return n, d


def mul (n1, d1, n2, d2):
    n = n1 * n2
    d = d1 * d2
    return n, d


def div (n1, d1, n2, d2):
    n = n1 * d2
    d = d1 * n2
    return n, d


def calc():
    try:
        n1 = int(num1.get())
        d1 = int(den1.get())
        n2 = int(num2.get())
        d2 = int(den2.get())
        operator = oper.get().strip()
        res = (0, 1)
        match operator:
            case "+": res = add (n1, d1, n2, d2)
            case "-": res = sub (n1, d1, n2, d2)
            case "*": res = mul (n1, d1, n2, d2)
            case "/": res = div (n1, d1, n2, d2)

        nod = math.gcd(res[0], res[1])

        n = int(res[0]/nod)
        d = int(res[1]/nod)
        int_p = ""
        if n > d:
            int_p = n // d
            n = n % d
        if n == 0:
            n = ""
            d = ""
        int_part.config(text=int_p)
        num3.config(text=n)
        den3.config(text=d)

    except Exception as e:
        print("ОШИБКА:", type(e).__name__, "—", e)

root = Tk()
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()
X = 300
Y = 140
root.geometry(f"{X}x{Y}+{WIDTH // 2 - X // 2}"
              f"+{HEIGHT // 2 - Y // 20}")
root.title('Proba')
frame = Frame(root)
frame.pack()

num1 = Entry(frame, width=2)
num1.config(font="Arial, 15",justify = "center")
num1.grid(row=0, column=0)
line1 = Label(frame, text = chr(8212)*3)
line1.grid(row=1, column=0)
den1 = Entry(frame, width=2)
den1.config(font="Arial, 15",justify = "center")
den1.grid(row=2, column=0)

oper = Entry(frame,font="Arial, 15")
oper.config(width=2, justify = "center")
oper.grid(row=1, column=1)

num2 = Entry(frame, width=2)
num2.config(font="Arial, 15",justify = "center")
num2.grid(row=0, column=2)
line2 = Label(frame, text = chr(8212)*3)
line2.grid(row=1, column=2)
den2 = Entry(frame, width=2)
den2.config(font="Arial, 15",justify = "center")
den2.grid(row=2, column=2)

btn = Button(frame, text = "=", width=2, command=calc)
btn.grid(row=1, column=3)

int_part = Label (frame, text = " ", bg = "lightgrey")
int_part.config(font="Arial, 20", width = 2, justify = "center")
int_part.grid(row=1, column=4)

num3 = Label(frame, width=2, bg = "lightgrey")
num3.config(font="Arial, 15",justify = "center")
num3.grid(row=0, column=5)
line3 = Label(frame, text = chr(8212)*3)
line3.grid(row=1, column=5)
den3 = Label(frame, width=2, bg = "lightgrey")
den3.config(font="Arial, 15",justify = "center")
den3.grid(row=2, column=5)

root.mainloop()

