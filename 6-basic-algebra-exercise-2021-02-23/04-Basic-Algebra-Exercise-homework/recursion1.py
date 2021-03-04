from turtle import *

def draw_branch(branch_length, angle, thickness):
    if branch_length > 5:
        if thickness <= 1: thickness = 1
        forward(branch_length)
        right(angle)
        pensize(thickness)
        draw_branch(branch_length - 15, angle, thickness - 2)
        left(2 * angle)
        pensize(thickness)
        draw_branch(branch_length - 15, angle, thickness - 2)
        right(angle)
        backward(branch_length)
        

# speed("fastest")
# left(90)
# draw_branch(100, 20)

def draw_tree(trunk_length, angle):
    pensize(10)
    speed("fastest")
    left(90)
    up()
    backward(trunk_length)
    down()
    draw_branch(trunk_length, angle, 10)
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

draw_tree(100, 60)
