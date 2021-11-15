# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
import leaderboard as lb

#-----game configuration----
colors = ["lightskyblue", "palegreen", "peachpuff", "plum"]
spot_color = "lightskyblue"
spot_shape = "turtle"
spot_size = 2

font_setup = ("System", 20, "bold")

score = 0

timer = 30
counter_interval = 1000
timer_up = False

leaderboard_file_name = "leaderboard.txt"
leader_names_list = []
leader_scores_list = []
name = input ("Your name: ")

#-----initialize turtle-----
spot = trtl.Turtle()
spot.fillcolor(spot_color)
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.pencolor(spot_color)

score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(-200,120)

counter = trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(50,120)

#-----game functions--------
def spot_clicked(x,y):
    global timer
    if timer > 0:
        update_score()
        change_position()
    else:
        spot.hideturtle()

def change_position():
    resize()
    recolor()
    new_xpos = rand.randint(-200,200)
    new_ypos = rand.randint(-150,80)
    spot.penup()
    spot.hideturtle()
    spot.goto(new_xpos,new_ypos)
    spot.showturtle()

def update_score():
    global score
    score = score + 1
    score_writer.clear() 
    score_writer.color("white") 
    score_writer.write("Score: " + str(score), font=font_setup)

def countdown():
  global timer, timer_up
  counter.clear()
  counter.color("white") 
  if timer <= 0:
    counter.write("Time's Up!", font=font_setup)
    timer_up = True
    spot.hideturtle()
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer = timer - 1
    counter.getscreen().ontimer(countdown, counter_interval)


def resize():
    sizes = [1, 1.5, 2, 2.5, 3, 3.5, 4]
    spot.shapesize(rand.choice(sizes))

def recolor():
    new_color = rand.choice(colors[0:])
    spot.fillcolor(new_color)
    spot.pencolor(new_color)

def start_game():
    spot.onclick(spot_clicked)
    counter.getscreen().ontimer(countdown, counter_interval)


def manage_leaderboard():
    global leader_scores_list
    global leader_names_list
    global score
    global spot
    lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

    if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
        lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, name, score)
        lb.draw_leaderboard(leader_names_list, leader_scores_list, True, spot, score)
    else:
        lb.draw_leaderboard(leader_names_list, leader_scores_list, False, spot, score)


#-----events----------------
wn = trtl.Screen()
wn.bgcolor("black")
spot.onclick(spot_clicked)
wn.ontimer(countdown, counter_interval) 
wn.mainloop()
