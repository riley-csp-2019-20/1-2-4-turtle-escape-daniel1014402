import turtle as trtl
import random
draw_Bot = trtl.Turtle()
Sgoat = trtl.Turtle()
draw_Bot.ht()

Sgoat.pensize(2)
Sgoat.color("cyan")
Sgoat.penup()
Sgoat.goto(159,279)
Sgoat.pendown()

amount = 15
draw_Bot.speed(0)
wall_width = 21
door_width = 20
draw_Bot.color("indigo")
draw_Bot.pensize(4)
barrier= 10

for i in range(25):
    if i > 4 and i < 22:
        door = random.randint(2*wall_width, amount - 2*wall_width)
        barrier = random.randint(2*wall_width, amount - 2*wall_width)

        if door < barrier:
            draw_Bot.forward(door)

            #door
            draw_Bot.penup()
            draw_Bot.forward(door_width)
            draw_Bot.pendown()

            draw_Bot.forward(barrier - door - door_width)

            #barrier
            draw_Bot.left(90)
            draw_Bot.forward(wall_width*2)
            draw_Bot.back(wall_width*2)
            draw_Bot.right(90)

            draw_Bot.forward(amount - barrier)

        else:
            draw_Bot.forward(barrier)

            #barrier
            draw_Bot.left(90)
            draw_Bot.forward(wall_width*2)
            draw_Bot.back(wall_width*2)
            draw_Bot.right(90)

            draw_Bot.forward(door - barrier)

            #door
            draw_Bot.penup()
            draw_Bot.forward(door_width)
            draw_Bot.pendown()

            draw_Bot.forward(amount - door - door_width)

        
    draw_Bot.left(90)
    amount += wall_width

def up():
    Sgoat.setheading(90)
    Sgoat.forward(9)

def right():
    Sgoat.setheading(0)
    Sgoat.forward(9)

def left():
    Sgoat.setheading(180)
    Sgoat.forward(9)

def down():
    Sgoat.setheading(270)
    Sgoat.forward(9)


wn = trtl.Screen()
wn.onkeypress(up,"Up")
wn.onkeypress(right,"Right")
wn.onkeypress(left,"Left")
wn.onkeypress(down,"Down")
wn.listen()
wn.bgcolor("beige")
wn.mainloop()