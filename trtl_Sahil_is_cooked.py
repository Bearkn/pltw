import turtle as trtl

# Set up the turtle
cube = trtl.Turtle()
cube.speed(5)

# Function to draw a square
def draw_square():
    for _ in range(4):
        cube.forward(100)
        cube.left(90)

# Draw front face
draw_square()

# Move to draw the back face connections
cube.left(45)
cube.forward(50)
cube.right(45)

# Draw back face
draw_square()

# Draw remaining edges
cube.goto(100, 0)
cube.left(45)
cube.forward(50)

cube.goto(100, 100)
cube.forward(50)

cube.goto(0, 100)
cube.forward(50)

# Hide turtle and keep window open
cube.hideturtle()
trtl.done()