# CODE TO COPY
#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)

#  
x = 0
y = 0
rot = 0
index = 0

#
for t in my_turtles:
  new_color = turtle_colors.pop()
  t.color(new_color)
  t.penup()
  t.goto(x, y)
  
  t.pendown()
  t.right(rot)     
  t.forward(50)


#	
  x = t.xcor()
  y = t.ycor()
  rot += 45
  index += 1

wn = trtl.Screen()
wn.mainloop()