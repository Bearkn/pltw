# a121_catch_a_turtle.py


#-----import statements-----
import turtle as t
import random as rand
import leaderboard as lb


#-----game configuration----
# leaderboard variables
leaderboard_file_name = "a122_leaderboard.txt"
player_name = input ("Please enter your name:")

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
scorer.teleport(350,350)
# scorer.showturtle()


timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False
counter = t.Turtle()
counter.hideturtle()
counter.penup()
counter.teleport(350,300)




#-----game functions--------
def countdown():
    global timer, timer_up
    counter.clear()
    if timer <= 0:
        counter.write("Time's Up", font=font_setup)
        timer_up = True
        leaderboard()
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
    global timer_up
    if timer_up == False: 
        change_position()
        update_score()
    elif timer_up == True:
        turt.hideturtle;
    
def change_position():
    new_xpos = rand.randint(-350,350)
    new_ypos = rand.randint(-350,350)
    # print("x", new_xpos)
    # print("y", new_ypos)
    turt.teleport(new_xpos, new_ypos);
    
def leaderboard():
    global score
    global spot

    # get the names and scores from the leaderboard file
    leader_names_list = lb.get_names(leaderboard_file_name)
    leader_scores_list = lb.get_scores(leaderboard_file_name)

    # show the leaderboard with or without the current player
    if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
        lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
        lb.draw_leaderboard(True, leader_names_list, leader_scores_list, turt, score)

    else:
        lb.draw_leaderboard(False, leader_names_list, leader_scores_list, turt, score)

#-----events----------------
turt.onclick(spot_clicked)
wn = t.Screen()
wn.ontimer(countdown, counter_interval) 
wn.mainloop()