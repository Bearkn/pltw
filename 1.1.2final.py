import turtle as trtl
import time

# Set up the screen
screen = trtl.Screen()
screen.bgcolor("white")
screen.setup(width=1600, height=600)
screen.tracer(0)  # Turn off automatic updates for smoother animation

# Create the ball
ball = trtl.Turtle()
ball.shape("circle")
ball.color("blue")
ball.penup()

# Get gravity from user
gravity = float(trtl.textinput("Gravity", "Enter gravity value (e.g., 0.5):"))

# Initial positions and velocities
x_pos = -400
y_pos = 200

x_vel = float(trtl.textinput("Horizontal Velocity", "Enter horizontal velocity (e.g., 5 to 20):"))
y_vel = float(trtl.textinput("Vertical Velocity", "Enter vertical velocity (e.g., 10):"))

bounce_factor = 0.7  # Energy loss on bounce
air_resistance = 0.99  # Multiplier to simulate air resistance

ball.goto(x_pos, y_pos)
ball.pendown()

# Animation loop
while True:

    # Apply gravity
    y_vel -= gravity

    # Update positions
    x_pos += x_vel
    y_pos += y_vel

    # Ground collision
    if y_pos <= -250:  # Assuming screen height is 600
        y_pos = -250
        y_vel = -y_vel * bounce_factor
        x_vel *= air_resistance  # Optional: simulate friction on ground bounce

    # Update turtle position
    ball.goto(x_pos, y_pos)

    # Update screen
    screen.update()
    time.sleep(0.01)

screen.mainloop()
