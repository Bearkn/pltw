import turtle as trtl

# import turtle module

# create turtle object
painter = trtl.Turtle()

# set the pen and fill colors
# then draw a circle
painter.pencolor("blue")
painter.fillcolor("light blue")
painter.begin_fill()
painter.circle(50)
painter.end_fill()

# move the turtle to another part of the screen
painter.penup()
painter.goto(100, 100)
painter.pendown()

# change both the pen and fill colors
# then draw a polygon of your choice
painter.pencolor("purple")
painter.fillcolor("pink")
painter.begin_fill()
for i in range(5):  # draws a pentagon
    painter.forward(50)
    painter.right(72)
painter.end_fill()

# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()