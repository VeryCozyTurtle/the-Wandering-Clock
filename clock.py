import turtle
import time
turtle.title('Wandering Clock')
# set the background color to black
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)

# Some other variables
tick = 0
tock = 0
click = 0
core = 0
angle1 = 0
angle2 = 0
angle3 = 0
angle4 = 0
angle5 = 0
angle6 = 0
angle7 = 0
b_homing_x = 0
b_homing_y = 0
petal = 0
tint = 0
tintsize = 0
pint = 0
pintsize = 0

# create amals
t = turtle.Turtle()
b = turtle.Turtle()
c = turtle.Turtle()
s = turtle.Turtle()
f = turtle.Turtle()
p = turtle.Turtle()
h = turtle.Turtle()
# set turtle position, orientation, size, color, and hide the turtles.
t.up()
t.goto(0, 0)
t.setheading(90)
t.pensize(20)
t.color("blue")
t.hideturtle()
t.clear()
# set bug position, orientation, size, color, and hide the turtles.
b.up()
b.goto(0, 0)
b.setheading(90)
b.pensize(3)
b.color(239,47,57)
b.hideturtle()
b.clear()
# set cat position, orientation, size, color, and hide the turtles.
c.up()
c.goto(0, 0)
c.setheading(90)
c.pensize(50)
c.color(239,47,57)
c.hideturtle()
c.clear()
# set snake position, orientation, size, color, and hide the turtles.
s.up()
s.goto(0, 0)
s.setheading(90)
s.pensize(2)
s.color(239,47,57)
s.hideturtle()
s.clear()
# set f position, orientation, size, color, and hide the turtles.
# This is the Frame of the Clock
f.up()
f.goto(0, 0)
f.setheading(270)
f.pensize(5)
f.color(201, 23, 19)
f.hideturtle()
f.clear()
f.bk(120)
f.right(90)
f.pendown()
f.circle(120)
f.penup()
# set pursuit position, orientation, size, color, and hide the turtles.
p.up()
p.goto(0, 0)
p.setheading(90)
p.pensize(2)
p.color(239,47,57)
p.hideturtle()
p.clear()
# set hub position, orientation, size, color, and hide the turtles.
h.up()
h.goto(0, 0)
h.setheading(90)
h.pensize(43)
h.color(239,47,57)
h.hideturtle()
h.clear()


# The main bulk of the clocks workings.
while True:

    # Clear the clock hands periodically
    if tock >= 1:
        t.clear()
        b.clear()
        a = b.position()
        c.goto(a)
        s.clear()
        c.clear()
        h.clear
        p.clear
        tock = 0
    tock += 1


    b.pendown()
    b.fd(100)
    b.rt(90)
    if tick/8 <= 10:
        core = 10
    else:
    
        core = tick/8
    if tick /8 >=25:
        core = 25
    #b.begin_fill()
    #b.circle(core)
    #b.end_fill()
    angle5 = p.towards(b)
    angle6 = p.towards(s)
    p.setheading(angle5 + angle6)
    p.pensize(petal)
    light = p.distance(b)
    petal = p.distance(c)
    if petal >= core:
        petal = core
    p.fd(petal*1.3)
    if light <= 50:
        click += 1
        if click >= 1:
            click = 0
            p.clear()
            p.pendown()
            pint += 1
            print()
            p.color((pint),47,57)
            p.fd(.001)
            p.bk(.001)
            if pint >=245:
                p.pensize(pintsize)
                p.color((pint),47,57)
                p.fd(distocore)
                p.bk(.001)
                pint = 0
                pintsize = pint/7
        p.penup()
        angle7 = p.towards(c)
        distocore = p.distance(c)
        p.setheading(angle7)
        p.fd(distocore)
        p.bk(distocore)
        #p.begin_fill()
        #p.circle(core/5)
        #p.end_fill()
        p.penup()
    b_homing_x = round(b.xcor(), 1)
    b_homing_y = round(b.ycor(), 1)
    b.rt(-90)
    b.penup()
    angle = b.towards(t)
    b.setheading(angle + tock)
    b.fd(100/1)
    angle = b.towards(t)
    b.setheading(angle)



    c.pensize(core)
    #c.pendown()
    c.fd(0.1)
    c.fd(-0.1)
    s.pendown()
    #s.goto(b_homing_x, b_homing_y)
    angle1 = s.towards(b)
    angle3 = angle1 + tick
    s.setheading(angle1)

    s.pensize(5)
    #s.begin_fill()
    #s.bk(100)
    s.fd(20)
    #s.end_fill()
    s.fd(30)
    s.penup()
    s.pensize(10)
    tick += 1
    if tick >= 255:
        tick = 0
    t.setheading(tick)
    #t.pendown()
    t.fd(110)
    t.bk(110)
    #t.penup()

    # This section keeps the hand from wandering away from the hub
    if b.distance(t) > 10:
        homing_x = round(t.xcor(), 1)
        homing_y = round(t.ycor(), 1)
        b.goto(homing_x, homing_y )

    
    h.pendown()
    h.fd(.001)
    h.bk(.001)
    tint += 1
    if tint >=255:
        h.clear()
        h.fd(.001)
        h.bk(.001)
        tint = 0
    h.penup()
    tintsize = tint/5
    h.pensize(tintsize)
    h.color((tint),47,57)
    





    print(tick, tock, click)
    # update the screen once all the drawing is done
    turtle.update()
    time.sleep(core/5)
    #time.sleep(.05)

#