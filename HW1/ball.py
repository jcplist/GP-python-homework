from vpython import *

g = 9.8 # g = 9.8 m/s^2
size = 0.25 # ball radius = 0.25 m
theta = pi/4
C_drag = 0.9 # drag coefficient = 0.9 1/s

scene = canvas(width=800, height=800, center =vec(0,7.5,0), background=vec(0.5,0.5,0)) # open a window
floor = box(length=30, height=0.01, width=10, color=color.blue) # the floor
ball = sphere(radius = size, color=color.red, make_trail = True, trail_radius = 0.05) # the ball

ball.pos = vec( -15, size, 0) # ball center initial position
ball.v = vec(20*cos(theta), 20*sin(theta) , 0) # ball initial velocity

dt = 0.001
count = 0 # count of ball bouncing
arrow_of_ball_v = arrow(color = color.green, shaftwidth = 0.05)

while count < 3:
    rate(1000)
    ball.pos += ball.v * dt
    ball.v -= C_drag * ball.v * dt
    ball.v.y -= g * dt
    arrow_of_ball_v.pos = ball.pos
    arrow_of_ball_v.axis = ball.v
    if ball.pos.y <= size and ball.v.y < 0:
        ball.v.y *= -1
        count += 1
arrow_of_ball_v.axis = vec(0, 0, 0)
