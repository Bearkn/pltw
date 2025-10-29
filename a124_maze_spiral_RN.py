#config
import turtle as t
import random as rand

maze_painter = t.Turtle()
maze_painter.hideturtle()
maze_painter.speed(0)

maze_runner = t.Turtle()
maze_runner.shape("turtle")
maze_runner.penup()
maze_runner.goto(0, 0)

# variables
'''The number of walls

The distance between walls, in other words, the width of the path

The turtle’s pen color to generate the walls.'''

maze_wall_number = 20;

maze_wall_width = 10;
# maze_wall_color = "blue"
wall_length = 10
door_location = 0
barrier_location = 0




#function
def draw_maze():
    global wall_length
    maze_painter.pencolor("blue")
    maze_painter.penup()
    maze_painter.goto(0, 0)
    maze_painter.pendown()
    
    for i in range(maze_wall_number):
        wall_length = maze_wall_width * i
        if i > 3:
            randomize_door_barrier_location()
            maze_painter.forward(door_location)
            maze_painter.penup()
            maze_painter.forward(maze_wall_width)
            maze_painter.pendown()
            draw_barrier()
            remaining = wall_length - door_location - maze_wall_width
            maze_painter.forward(remaining)
        else:
            maze_painter.forward(wall_length)
        maze_painter.left(90)


def draw_door():
    
    maze_painter.forward(door_location)
    maze_painter.penup()
    maze_painter.forward(maze_wall_width)
    maze_painter.pendown()
    draw_barrier()
    
def draw_barrier():
    maze_painter.forward(40)
    maze_painter.left(90)
    maze_painter.forward(maze_wall_width*2)
    maze_painter.back(maze_wall_width*2)
    maze_painter.right(90)
    
def randomize_door_barrier_location():
    global wall_length
    global door_location
    global barrier_location
    # randomize location of doors and barriers in wall
    door_location = rand.randint(maze_wall_width*2, (wall_length - maze_wall_width*2))
    barrier_location = rand.randint(maze_wall_width*2, (wall_length - maze_wall_width*2))

def move_up():
    maze_runner.setheading(90)
    maze_runner.forward(10)

def move_down():
    maze_runner.setheading(270)
    maze_runner.forward(10)

def move_left():
    maze_runner.setheading(180)
    maze_runner.forward(10)

def move_right():
    maze_runner.setheading(0)
    maze_runner.forward(10)
        
draw_maze()

wn = t.Screen()

wn.onkeypress(move_up, "Up")
wn.onkeypress(move_down, "Down")
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.listen()

wn.mainloop()