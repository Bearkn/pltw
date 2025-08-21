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


# Initial positions and velocities
x_pos = -800
y_pos = 10
# gravity = float(trtl.textinput("Gravity", "Enter gravity value (e.g., 0.5):"))
# x_vel = float(trtl.textinput("Horizontal Velocity", "Enter horizontal velocity (e.g., 5 to 20):"))
# y_vel = float(trtl.textinput("Vertical Velocity", "Enter vertical velocity (e.g., 10):"))
# spin = float(trtl.textinput("Spin", "Enter initial spin value (e.g., 5 for clockwise, -5 for counterclockwise):"))
gravity = float(.5)
x_vel = float(40)
y_vel = float(3)
spin = float(trtl.textinput("Spin", "Enter initial spin value (e.g., 5 for clockwise, -5 for counterclockwise):"))
spin_friction = 0.98  # Reduces spin over time

bounce_factor = 0.7  # Energy loss on bounce
air_resistance = 0.98  # Multiplier to simulate air resistance

ball.goto(x_pos, y_pos)
ball.pendown()

# Animation loop
while True:
    ball.right(spin)
    # Apply gravity
    y_vel -= gravity

    # Update positions
    x_pos += x_vel
    y_pos += y_vel

    # Ground collision
    if y_pos <= -250:
        y_pos = -250
        y_vel = -y_vel * bounce_factor

        # Simulate interaction between spin and ground affecting horizontal velocity
        x_vel += spin * 0.05  # Smaller factor for more realistic push from spin

        # Dampen spin and horizontal velocity (simulates friction)
        x_vel *= air_resistance
        spin *= 0.9  # Reduce spin due to friction on ground
    
        # Apply rolling resistance when ball is nearly done bouncing
    if abs(y_vel) < 1:
        x_vel *= 0.96  # Tweak this factor for stronger rolling resistance
        spin *= spin_friction  # Spin slows over time    
    # Update turtle position
    ball.goto(x_pos, y_pos)
    # Stop the ball if it slows down enough
    if abs(x_vel) < 0.05 and abs(y_vel) < 0.1:
        x_vel = 0
        y_vel = 0
        spin = 0
        
    if(x_pos > 800 or x_pos < -800):
        x_vel = -x_vel
    # Update screen
    screen.update()
    time.sleep(0.01)

screen.mainloop()
