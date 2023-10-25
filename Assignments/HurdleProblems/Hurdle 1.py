def turn_right():
    turn_left()
    turn_left()
    turn_left()
def move_a_block(): 
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
while not at_goal():
    move_a_block()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
