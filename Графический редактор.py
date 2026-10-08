from tkinter import *


def draw(event):
    x, y = event.x, event.y
    w = pen_width.get()
    color = pen_color.get()
    canvas.create_oval(x, y, x + w, y + w,
                       fill=color, outline=color)
def set_pen_width():
    try:
        pen_width.set(int(pen_input.get()))
    except ValueError:
        pass




window = Tk()
window.title("Рисование на холсте")
pen_color = StringVar(value="red")
pen_width = IntVar(value=5)
canvas = Canvas(window, width=600, height=400)
canvas.pack()
canvas.bind("<B1-Motion>", draw)

colors = ["red", "green", "blue", "black"]
for color in colors:
    lbl = Label(window, text="", bg=color, width=8, height=2)
    lbl.pack(side=LEFT)
    lbl.bind("<Button-1>", lambda e, c=color: pen_color.set(c))


btn_frame = Frame(window)
btn_frame.pack(side=BOTTOM)

pen_label = Label(btn_frame, text="Pen width")
pen_label.pack(side=LEFT)

pen_input = Entry(btn_frame, width=10)
pen_input.pack(side=LEFT)

btn = Button(btn_frame, text="Set pen width", command=set_pen_width)
btn.pack()

window.mainloop()