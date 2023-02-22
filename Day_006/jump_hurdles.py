import random

# This really doesnt make much sense 
# but can be used here:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json


def turn_left():
    print('Left')


def move():
    print('Move')


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    print('jump>')
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


# - this is sufficient for hurdles_1
#for i in range(1, 7):
#    jump()

def at_goal():
    return random.random() > 0.8


def wall_in_front():
    return random.random() > .3


def move_wall_up_and_down():
    # we know we are facing a
    # wall here
    num_steps = 0
    while wall_in_front():
        turn_left()
        move()
        turn_right()
        num_steps += 1
    
    move()
    turn_right()
    
    for n in range(0, num_steps):
        move()
    
    turn_left()
    

while not at_goal():
    if wall_in_front():
        move_wall_up_and_down()
    else:
        move()
