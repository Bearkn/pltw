#config
import turtle as t
import random as rand

maze_painter = t.Turtle()
maze_painter.hideturtle()
maze_painter.speed(0)

maze_runner = t.Turtle()

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

def runner_movement(direction):
    if(direction == "up"):
        maze_runner.up()
    elif(direction == "down"):
        maze_runner.down()
    elif(direction == "right"):
        maze_runner.goto(maze_runner.xcor + 10,maze_runner.ycor)
    elif(direction == "left"):
        maze_runner.goto(maze_runner.xcor - 10,maze_runner.ycor)
draw_maze()

wn = t.Screen()
wn.onkeypress(runner_movement("up"),"w")
wn.listen()
wn.mainloop()