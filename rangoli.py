#importing Turtle module
import turtle
a=turtle.Turtle()
#Setting the screen to 700,700
turtle.setup(700,700)
#Title of the window
turtle.title("Happy Diwali 2021")
a.up()
a.goto(-180,235)
a.down()
turtle.bgcolor("Black")
#Created the function for Square
def square(length,angle):
    for i in range(4):
        a.forward(length)
        a.right(angle)

for i in range(10):
       a.color('black','yellow')
       a.speed(200)
       a.pensize(2)
       a.begin_fill()
       square(280, 60)
       a.right(12)
       a.end_fill()


a.up()
a.goto(0,-8)
a.down()
#Created the function for Outer Semi-Circle
for i in range(8):
    a.speed(100)
    a.color("black","orange")
    a.begin_fill()
    a.circle(140)
    a.left(45)
    a.end_fill()

# Navy Blue Outer circle 2    

a.penup()
a.goto(0,-250)
a.pendown()
a.pensize(22)
a.color("#ADD8E6")
a.begin_fill()
a.circle(250)
a.end_fill()

# Green outer circle 3
a.penup()
a.goto(0,-230)
a.pendown()
a.pensize(21)
a.color("green")
a.circle(230)

a.speed(100)
a.up()
a.goto(0,-218)
a.pensize(10)
a.color("brown","yellow")
a.begin_fill()
a.circle(220)
a.end_fill()
a.goto(0,-175)




#Created the function for inner circle

def outc(x):
    for k in range(3):
      for j in range(12):
        for i in range(36):
          if(i%2==0):
            a.color("#D04801")
          else:
            a.color("#FAD9F4")
          a.circle(x,10)
        x=x-1
        a.lt(90)
        a.forward(1)
        a.rt(90)
        a.circle(x,1)
      a.circle(x,10)
def mid():
  a.lt(45)
  a.color("#92141F")
  a.begin_fill()
  for i in range(30):
    a.forward(1)
    a.lt(1)
  a.circle(10,270)
  a.rt(80)
  a.forward(20)
  a.lt(170)
  a.end_fill()
  a.pu()
  a.forward(30)
  a.pd()
  a.color("white")
  a.begin_fill()
  a.circle(3)
  a.end_fill()
  a.pu()
  a.rt(170)
  a.forward(30)
  a.lt(100)
def out():
  a.color("#344C29")
  a.begin_fill()
  a.rt(60)
  a.forward(30)
  a.rt(50)
  a.forward(45)
  a.rt(140)
  a.forward(45)
  a.rt(50)
  a.forward(30)
  a.rt(60)
  a.end_fill()
  a.pencolor("black")
def pattern():
  a.lt(90)
  a.circle(40,90)
  for i in range(3):
    a.lt(180)
    a.circle(40,90)
a.speed(0)
a.rt(90)
a.pu()
a.forward(30)
a.lt(90)
a.pd()
a.color("#EE5F11")
a.begin_fill()
a.circle(210)
a.end_fill()
a.rt(90)
a.pu()
a.bk(30)
a.pd()
a.lt(90)
# Inner rainbow circle

for i in range(16):
  a.circle(180,22.5)
  out()
a.color("#ECC92D")
a.begin_fill()
a.circle(178)
a.end_fill()

for i in range(13):
  mid()
  a.pu()
  a.circle(200,22.5)
  a.pd()
a.pu()
a.lt(90)
a.forward(41)
a.rt(90)
a.pd()
a.circle(135)
outc(135)
a.color("brown")
a.begin_fill()
a.circle(100)
a.end_fill()

# stars in the centre
for i in range(6):
  if(i%2==0):
    a.fillcolor("#F9D22F")
  else:
    a.fillcolor("#FC8D08")
  a.pu()
  a.circle(100,60)
  a.pd()
  a.begin_fill()
  pattern()
  a.lt(90)
  a.end_fill()
a.pu()



turtle.hideturtle()

turtle.done()
# Created by: Swastik Mishra