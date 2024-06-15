import turtle

turtle.speed(20)

turtle.penup()
turtle.left(90)
turtle.forward(100)
# Head

turtle.pensize(5)
turtle.left(90)
turtle.pendown()
turtle.circle(125, 50)
turtle.penup()
turtle.circle(125, 25)
turtle.pendown()
turtle.circle(125, 105)
turtle.right(90)

# Neck
turtle.forward(100)
turtle.right(63)
turtle.pensize(5)
turtle.circle(-125, 60)
turtle.circle(-50, -60)
turtle.circle(-50, -65)
turtle.forward(-55)
turtle.end_fill()

# Eyes 1
turtle.penup()
turtle.pensize(5)
turtle.right(175)
turtle.forward(169.5)
turtle.left(130)
turtle.pendown()
turtle.circle(-50, 85)
turtle.circle(-45, 30)

# Pilok
turtle.penup()
turtle.left(45)
turtle.forward(25)
turtle.right(180)
turtle.pendown()
turtle.pensize(5)
turtle.circle(50, 60)
turtle.circle(-35, 130)

# Eyes 2
turtle.pensize(5)
turtle.penup()
turtle.left(100)
turtle.forward(75)
turtle.pendown()
turtle.right(60)
turtle.circle(50, 85)
turtle.circle(45, 30)

# Pilok
turtle.penup()
turtle.left(122)
turtle.forward(83.5)
turtle.right(115)
turtle.pendown()
turtle.pensize(5)
turtle.circle(-50, 30)
turtle.circle(-35, 80)
turtle.circle(35, 90)

# Nose
turtle.penup()
turtle.left(145)
turtle.forward(170)
turtle.pendown()
turtle.pensize(5)
turtle.forward(15)
turtle.circle(15, 120)
turtle.forward(15)

# Mouth
turtle.penup()
turtle.forward(75)
turtle.left(100)
turtle.pendown()
turtle.circle(-45, 80)

# Eyes1
turtle.penup()
turtle.left(115)
turtle.forward(125)
turtle.left(140)
turtle.pendown()
turtle.pensize(5)
turtle.circle(27.5, 90)
turtle.circle(15, 90)

# Eyes2
turtle.penup()
turtle.left(119)
turtle.forward(180)
turtle.left(60)
turtle.pendown()
turtle.circle(28, 100)
turtle.circle(20, 90)

# Eyebrows1
turtle.penup()
turtle.left(60)
turtle.forward(74.5)
turtle.pendown()
turtle.pensize(10)
turtle.left(60)
turtle.circle(100, 10)

# Eyebrows2
turtle.penup()
turtle.left(175)
turtle.forward(175)
turtle.pendown()
turtle.right(20)
turtle.circle(100, 10)

# Hair
turtle.penup()
turtle.left(195)
turtle.forward(150)
turtle.right(125)
turtle.pendown()
turtle.pensize(5)
turtle.circle(-150, 50)
turtle.left(100)
turtle.penup()
turtle.forward(25)
turtle.left(180)
turtle.pendown()
turtle.circle(200, 50)
turtle.right(110)
turtle.circle(400, 47)
turtle.left(65)
turtle.circle(200, 40)
turtle.left(470)
turtle.circle(-200, 50)
turtle.forward(350)
turtle.left(109)
turtle.forward(180)
turtle.circle(50, 35)
turtle.circle(200, 43)

turtle.hideturtle()
turtle.done()
