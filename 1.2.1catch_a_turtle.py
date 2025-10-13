# a121_catch_a_turtle.py


#-----import statements-----
import turtle as t
import random as rand

#-----game configuration----
spot_color = "pink"
spot_size = 2
spot_shape = "circle"
score = 0

font_setup = ("Arial", 20, "normal")


#-----initialize turtle-----

turt = t.Turtle()
turt.shape(spot_shape)
turt.shapesize(spot_size)
turt.fillcolor(spot_color)
turt.penup()

scorer = t.Turtle()
scorer.hideturtle()
scorer.penup()
scorer.goto(350,350)
# scorer.showturtle()


timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False
counter = t.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(350,300)


#-----game functions--------
def countdown():
    global timer, timer_up
    counter.clear()
    if timer <= 0:
        counter.write("Time's Up", font=font_setup)
        timer_up = True
    else:
        counter.write("Timer: " + str(timer), font=font_setup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counter_interval) 
def update_score():
    global score
    score += 1
    scorer.clear()
    scorer.write(score, font=font_setup)
def spot_clicked(x,y):
    change_position()
    update_score()
    
def change_position():
    turt.hideturtle()
    new_xpos = rand.randint(-350,350)
    new_ypos = rand.randint(-350,350)
    print("x", new_xpos)
    print("y", new_ypos)
    turt.goto(new_xpos, new_ypos);
    turt.showturtle()

#-----events----------------
turt.onclick(spot_clicked)
wn = t.Screen()
wn.ontimer(countdown, counter_interval) 
wn.mainloop()