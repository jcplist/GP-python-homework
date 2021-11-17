#######################################################
##lesson 5 homework？ What is lesson 5 homework？？？##
##lesson 5 homework？ What is lesson 5 homework？？？##
##lesson 5 homework？ What is lesson 5 homework？？？##
#######################################################
import numpy as np
from vpython import *
A, N, omega = 0.10, 50, 2*pi/1.0
size, m, k, d = 0.06, 0.1, 10.0, 0.4
scene = canvas(title='Spring Wave', width=800, height=300, background=vec(0.5,0.5,0), center = vec((N-1)*d/2, 0, 0))
#1
ball_pos, ball_orig, ball_v, spring_len = np.arange(N)*d, np.arange(N)*d, np.zeros(N), np.ones(N)*d #5
t, dt = 0, 0.001
c = curve([vector(i*d, 1.0, 0) for i in range(N)], color=color.black)
while True:
    rate(1000)
    t += dt
    ball_pos[0] = A * sin(omega * t ) #4
    spring_len[:-1] = ball_pos[1:] - ball_pos[:-1]
    ball_v[1:] += k * (spring_len[1:]-spring_len[:-1]) / m * dt#6
    ball_pos += ball_v*dt
    ball_disp = ball_pos - ball_orig
    for i in range(N):
        c.modify(i, y = ball_disp[i]*4+1)
