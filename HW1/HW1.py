from vpython import *

g = 9.8 # g = 9.8 m/s^2
size = 0.25 # ball radius = 0.25 m
theta = pi/4
C_drag = 0.9 # drag coefficient = 0.9 1/s

scene = canvas(width=800, height=800, center =vec(0,size/2,0), background=vec(0.5,0.5,0)) # open a window
floor = box(length=30, height=0.01, width=10, color=color.blue) # the floor
ball = sphere(radius = size, color=color.red, make_trail = True, trail_radius = 0.05) # the ball
chart = graph(width = 450, align = 'left')

ball.pos = vec( -15, size, 0) # ball center initial position
ball.v = vec(20*cos(theta), 20*sin(theta) , 0) # ball initial velocity

dt = 0.001
count = 0 # count of ball bouncing
arrow_of_ball_v = arrow(color = color.green, shaftwidth = 0.05)
v_t = gcurve(graph = chart, color = color.blue, width = 4)
t = 0
d = 0
td = 0
lh = 0
msg = label(text = '',pos = vec(-10, 12, 0), box = False)

while count < 3:
    rate(1000)
    ball.pos += ball.v * dt
    td += ball.v.mag * dt
    ball.v -= C_drag * ball.v * dt
    ball.v.y -= g * dt
    arrow_of_ball_v.pos = ball.pos
    arrow_of_ball_v.axis = ball.v
    t += dt
    v_t.plot(pos = (t,ball.v.mag))
    if lh < ball.pos.y:
        lh = ball.pos.y
    d = ((ball.pos.x + 15)**2 + (ball.pos.y - size)**2)**0.5
    msg.text = 'displacement = ' + str(d) +'\ntotal distance = ' + str(td) + '\nlargest height = ' + str(lh)
    if ball.pos.y <= size and ball.v.y < 0:
        ball.v.y *= -1
        count += 1
arrow_of_ball_v.axis = vec(0, 0, 0)
