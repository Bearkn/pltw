# import the turtle module
import turtle as trtl

# create the turtle object
painter = trtl.Turtle()

print("making a circle...")

# ask user for a color (such as red, green, blue, pink, purple)
print("what color do you want")
color_of_circle = input()
# ask user for the radius of a circle
print("what radius")
radius_of_circle = int(input())

# draw a circle with the radius and line color entered by the user
painter.color(color_of_circle)
painter.circle(radius_of_circle)

# get the screen object and make it persist

wn = trtl.Screen()
wn.mainloop()