from random import randint
from time import sleep
from turtle import *
#
# colormode(255)
# shape('turtle')
# color((117, 2, 84), (191, 33, 142))
# pensize(4)
# speed(20)
#
# # r = 100
# # g = 33
# # b = 142
# # step = 0
# # for i in range(200, 10, -20):
# #     fillcolor(r, g, b)
# #     for _ in range(6):
# #         begin_fill()
# #         # circle(i)
# #         for _ in range(3):
# #             forward(i)
# #             left(120)
# #         end_fill()
# #         rt(60)
# #     r += 15
# #     g += 10
# #     b += 5
# #
# #
# #     penup()
# #     step-=200
# #     goto(0, 0)
# #     pendown()
# #
# # mainloop()
# def draw_lanscape():
#     penup()
#     goto(-200, -200)
#     pendown()
#     color('lightgreen')
#     begin_fill()
#     for i in range(2):
#         forward(400)
#         left(90)
#         forward(150)
#         left(90)
#     end_fill()
#
#
# def draw_sky():
#     penup()
#     goto(-200, -50)
#     pendown()
#     color('lightblue')
#     begin_fill()
#     for i in range(2):
#         forward(400)
#         left(90)
#         forward(300)
#         left(90)
#     end_fill()
#
# def draw_sun():
#     penup()
#     goto(120, 150)
#     pendown()
#     color('yellow')
#     begin_fill()
#     for i in range(1):
#         circle(20)
#     end_fill()
#
# def draw_house():
#     penup()
#     goto(-150, -110)
#     pendown()
#     color('grey')
#     begin_fill()
#     for i in range(2):
#         forward(100)
#         left(90)
#         forward(170)
#         left(90)
#     end_fill()
#
# def draw_windows():
#     # penup()
#     # goto(-130, -70)
#     # pendown()
#     color('yellow')
#     begin_fill()
#     for i in range(4):
#         forward(15)
#         left(90)
#     end_fill()
#     # penup()
#     # goto(-90, -70)
#     # pendown()
#     # begin_fill()
#     # for i in range(4):
#     #     forward(20)
#     #     left(90)
#     # end_fill()
#     # penup()
#     # goto(-90, -30)
#     # pendown()
#     # begin_fill()
#     # for i in range(4):
#     #     forward(20)
#     #     left(90)
#     # end_fill()
#     # penup()
#     # goto(-130, -30)
#     # pendown()
#     # begin_fill()
#     # for i in range(4):
#     #     forward(20)
#     #     left(90)
#     # end_fill()
#     # penup()
#     # goto(-90, 10)
#     # pendown()
#     # begin_fill()
#     # for i in range(4):
#     #     forward(20)
#     #     left(90)
#     # end_fill()
#     # penup()
#     # goto(-130, 10)
#     # pendown()
#     # begin_fill()
#     # for i in range(4):
#     #     forward(20)
#     #     left(90)
#     # end_fill()
#
# def draw_pharmacy():
#     penup()
#     goto(70, -110)
#     pendown()
#     color('brown', 'goldenrod')
#     begin_fill()
#     for i in range(4):
#         forward(70)
#         left(90)
#     end_fill()
#     penup()
#     goto(90, -65)
#     pendown()
#     color('red')
#     forward(20)
#     penup()
#     goto(100, -55)
#     pendown()
#     right(90)
#     forward(20)
#
# # draw_lanscape()
# # draw_sky()
# # draw_sun()
# # draw_house()
# # draw_windows()
# # draw_pharmacy()
# # penup()
# # goto(300, 300)
# penup()
# goto(-170, -170)
# pendown()
# color('brown')
# begin_fill()
# for i in range(2):
#     forward(100)
#     left(90)
#     forward(210)
#     left(90)
# end_fill()
# for row in range(6):
#     for col in range(2):
#         penup()
#         goto(-145+col * 30, -145 + row*30)
#         print(xcor(), ycor())
#         pendown()
#         pendown()
#         draw_windows()
#
# penup()
# goto(-160, -160)
#

w = 300
h = 300

penup()
goto(-300,-300)
pendown()
color('lightgreen')
penup()
pendown()
speed(20)
begin_fill()
for i in range(4):
    forward(w*2)
    left(90)
end_fill()

t1 = Turtle()
t1.color('red')
t1.shape('turtle')
t1.width(5)

t2 = Turtle()
t2.color('blue')
t2.shape('turtle')
t2.left(240)
t2.width(5)

t3 = Turtle()
t3.color('yellow')
t3.shape('turtle')
t3.shape('turtle')
t3.left(120)
t3.width(5)

def catcht1(x,y):
    t1.penup()
    t1.goto(randint(-300,300),randint(-300,300))
    t1.pendown()
    t1.left(randint(0, 180))



def catcht2(x,y):
    t2.penup()
    t2.goto(randint(-300,300),randint(-300,300))
    t2.pendown()
    t2.left(randint(0, 180))


def catcht3(x, y):
    t3.penup()
    t3.goto(randint(-300, 300), randint(-300, 300))
    t3.pendown()
    t3.left(randint(0, 180))


def game_over(t1, t2, t3):
    t1_outside = abs(t1.xcor()) > w or abs(t1.ycor()) > h
    t2_outside = abs(t2.xcor()) > w or abs(t2.ycor()) > h
    t3_outside = abs(t3.xcor()) > w or abs(t3.ycor()) > h
    t_outside = t1_outside or t2_outside or t3_outside
    return t_outside

t1.onclick(catcht1)
t2.onclick(catcht2)
t3.onclick(catcht3)

while game_over(t1, t2, t3) != True:
    t1.forward(7)
    t2.forward(10)
    t3.forward(3)
    sleep(0.1)
else:
    penup()
    print("Game Over")
    pendown()

t1.clear()
t2.clear()
t3.clear()
t1.penup()
t2.penup()
t3.penup()
t1.goto(-130,0)
t1.write('Game over', font=('Arial', 50, 'bold'))
t1.goto(-120, -20)
t1.left(360)
t2.goto(0,-20)
t2.left(360)
t3.goto(120,-20)
t3.left(360)





mainloop()