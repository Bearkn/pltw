import turtle as trtl

# import turtle module

# create turtle object
painter = trtl.Turtle()

# add code here for a circle
painter.circle(50)  # draws a circle with radius 50

# move the turtle to another part of the screen
painter.penup()
painter.goto(100, 0)  # moves 100 pixels to the right
painter.pendown()

# add code here for an arc
painter.circle(50, 180)  # draws a half circle (180 degrees)

# move the turtle to another part of the screen
painter.penup()
painter.goto(-100, 0)  # moves 100 pixels to the left
painter.pendown()

# add code here for an arc that is greater than 
painter.circle(50, 270)  # draws a 270 degree arc

# keep the window open
wn = trtl.Screen()
wn.mainloop()