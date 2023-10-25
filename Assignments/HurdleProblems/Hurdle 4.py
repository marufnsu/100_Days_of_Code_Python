def turn_right():
    turn_left()
    turn_left()
    turn_left()
def move_a_block(): 
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
while not at_goal():
    if wall_in_front():
        move_a_block()
    else:
        move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
