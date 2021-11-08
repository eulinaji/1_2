# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
import leaderboard as lb

#-----game configuration----
colors = ["black", "sky blue", "salmon", "orchid", "pale green"]
spot_color = "salmon"
spot_shape = "square"
spot_size = 2

font_setup = ("System", 20, "normal")

score = 0

timer = 5
counter_interval = 1000
timer_up = False

leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input ("Please enter your name:")

#-----initialize turtle-----
spot = trtl.Turtle()
spot.fillcolor(spot_color)
spot.shape(spot_shape)
spot.shapesize(spot_size)

score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(-250,200)

counter =  trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(150,200)

#-----game functions--------
def spot_clicked(x,y):
    global timer
    if timer > 0:
        update_score()
        change_position()
    else:
        spot.hideturtle()

def change_position():
    leave_mark()
    resize()
    new_xpos = rand.randint(-300,300)
    new_ypos = rand.randint(-300,300)
    spot.penup()
    spot.hideturtle()
    spot.goto(new_xpos,new_ypos)
    spot.showturtle()

def update_score():
    global score
    score = score + 1
    score_writer.clear()  
    score_writer.write(score, font=font_setup)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()

  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer = timer - 1
    counter.getscreen().ontimer(countdown, counter_interval)

def resize():
    sizes = [0.5, 1, 1.5, 2]
    spot.shapesize(rand.choice(sizes))

def leave_mark():
    spot.fillcolor(rand.choice(colors[1:]))
    spot.stamp()
    spot.fillcolor(colors[0])

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
        lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
        lb.draw_leaderboard(leader_names_list, leader_scores_list, True, spot, score)
    else:
        lb.draw_leaderboard(leader_names_list, leader_scores_list, False, spot, score)

#-----events----------------
wn = trtl.Screen()
wn.bgcolor("peachpuff")
spot.onclick(spot_clicked)
# wn.ontimer(countdown, counter_interval) 
wn.mainloop()
