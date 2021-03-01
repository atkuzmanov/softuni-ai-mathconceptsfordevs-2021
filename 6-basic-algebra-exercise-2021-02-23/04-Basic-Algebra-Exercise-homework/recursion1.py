from turtle import *

def draw_branch(branch_length, angle):
    if branch_length > 5:
        forward(branch_length)
        right(angle)
        draw_branch(branch_length - 15, angle)
        left(2 * angle)
        draw_branch(branch_length - 15, angle)
        right(angle)
        backward(branch_length)

# speed("fastest")
# left(90)
# draw_branch(100, 20)

def draw_tree(trunk_length, angle):
    speed("fastest")
    left(90)
    up()
    backward(trunk_length)
    down()
    draw_branch(trunk_length, angle)
    done()

# draw_tree(100, -20)

# draw_tree(100, 0)

# draw_tree(100, 5)

# draw_tree(100, 10)

# draw_tree(100, 15)

# draw_tree(100, 20)

# draw_tree(100, 30)

# draw_tree(100, 45)

# draw_tree(100, 60)

# draw_tree(100, 90)

# draw_tree(100, 180)

# draw_tree(100, 270)

# draw_tree(100, 360)
