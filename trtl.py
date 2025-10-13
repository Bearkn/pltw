# import turtle
# import math

# # Set up the turtle
# t = turtle.Turtle()
# t.speed(0)  # Fastest speed
# screen = turtle.Screen()
# screen.bgcolor("beige")

# # Draw face outline
# t.penup()
# t.goto(-100, 100)
# t.pendown()
# t.color("saddlebrown")
# t.begin_fill()
# for _ in range(2):
#     t.forward(200)
#     t.right(90)
#     t.forward(250)
#     t.right(90)
# t.end_fill()

# # Draw smile
# t.penup()
# t.goto(-30, 0)
# t.pendown()
# t.color("black")
# t.setheading(-60)
# t.circle(40, 120)

# # Draw eyes
# for x in (-30, 30):
#     t.penup()
#     t.goto(x, 50)
#     t.pendown()
#     t.circle(10)

# # Draw nose
# t.penup()
# t.goto(0, 30)
# t.pendown()
# t.setheading(-90)
# t.forward(20)

# # Draw hair
# t.penup()
# t.goto(-100, 100)
# t.color("darkbrown")
# t.pendown()
# for x in range(20):
#     t.forward(200)
#     t.right(170)
#     t.forward(200)

# screen.exitonclick()
