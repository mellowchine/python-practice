from turtle import *

colormode(255)
shape('turtle')
color((117, 2, 84), (191, 33, 142))
pensize(4)
speed(20)

# r = 100
# g = 33
# b = 142
# step = 0
# for i in range(200, 10, -20):
#     fillcolor(r, g, b)
#     for _ in range(6):
#         begin_fill()
#         # circle(i)
#         for _ in range(3):
#             forward(i)
#             left(120)
#         end_fill()
#         rt(60)
#     r += 15
#     g += 10
#     b += 5
#
#
#     penup()
#     step-=200
#     goto(0, 0)
#     pendown()
#
# mainloop()
def draw_lanscape():
    penup()
    goto(-200, -200)
    pendown()
    color('lightgreen')
    begin_fill()
    for i in range(2):
        forward(400)
        left(90)
        forward(150)
        left(90)
    end_fill()


def draw_sky():
    penup()
    goto(-200, -50)
    pendown()
    color('lightblue')
    begin_fill()
    for i in range(2):
        forward(400)
        left(90)
        forward(300)
        left(90)
    end_fill()

def draw_sun():
    penup()
    goto(120, 150)
    pendown()
    color('yellow')
    begin_fill()
    for i in range(1):
        circle(20)
    end_fill()

def draw_house():
    penup()
    goto(-150, -110)
    pendown()
    color('grey')
    begin_fill()
    for i in range(2):
        forward(100)
        left(90)
        forward(170)
        left(90)
    end_fill()

def draw_windows():
    penup()
    goto(-130, -70)
    pendown()
    color('white')
    begin_fill()
    for i in range(4):
        forward(20)
        left(90)
    end_fill()
    penup()
    goto(-90, -70)
    pendown()
    begin_fill()
    for i in range(4):
        forward(20)
        left(90)
    end_fill()
    penup()
    goto(-90, -30)
    pendown()
    begin_fill()
    for i in range(4):
        forward(20)
        left(90)
    end_fill()
    penup()
    goto(-130, -30)
    pendown()
    begin_fill()
    for i in range(4):
        forward(20)
        left(90)
    end_fill()
    penup()
    goto(-90, 10)
    pendown()
    begin_fill()
    for i in range(4):
        forward(20)
        left(90)
    end_fill()
    penup()
    goto(-130, 10)
    pendown()
    begin_fill()
    for i in range(4):
        forward(20)
        left(90)
    end_fill()

def draw_pharmacy():
    penup()
    goto(70, -110)
    pendown()
    color('brown', 'goldenrod')
    begin_fill()
    for i in range(4):
        forward(70)
        left(90)
    end_fill()
    penup()
    goto(90, -65)
    pendown()
    color('red')
    forward(20)
    penup()
    goto(100, -55)
    pendown()
    right(90)
    forward(20)

draw_lanscape()
draw_sky()
draw_sun()
draw_house()
draw_windows()
draw_pharmacy()
penup()
goto(300, 300)
exitonclick()