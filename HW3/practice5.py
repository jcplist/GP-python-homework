#######################################################
##lesson 5 homework？ What is lesson 5 homework？？？##
##lesson 5 homework？ What is lesson 5 homework？？？##
##lesson 5 homework？ What is lesson 5 homework？？？##
#######################################################
import numpy as np
from vpython import *
A, N = 0.10, 50
size, m, k, d = 0.06, 0.1, 10.0, 0.4
scene = canvas(title='Spring Wave', width=800, height=300, background=vec(0.5,0.5,0), center = vec((N-1)*d/2, 0, 0))
#1
Unit_K, n = 2 * pi/(N*d), 10
Wavevector = n * Unit_K
phase = Wavevector * arange(N) * d
ball_pos, ball_orig, ball_v, spring_len = np.arange(N)*d + A*np.sin(phase), np.arange(N)*d, np.zeros(N), np.ones(N)*d #5
t, dt = 0, 0.0003
t_of_largest, t_of_smallest, T = 0, 0, 0
c = curve([vector(i*d, 1.0, 0) for i in range(N)], color=color.black)
while True:
    rate(5000)
    t += dt
    spring_len[:-1] = ball_pos[1:] - ball_pos[:-1]
    spring_len[-1] = ball_pos[0]-ball_pos[-1] + N*d
    ball_v[1:] += k * (spring_len[1:]-spring_len[:-1]) / m * dt#6
    ball_v[0] += k * (spring_len[0]-spring_len[-1]) / m * dt
    ball_pos += ball_v*dt
    ball_disp = ball_pos - ball_orig
    for i in range(N):
        c.modify(i, y = ball_disp[i]*4+1)
    if T==0 :
        if ball_v[1] < 0 and ball_v[1]-k * (spring_len[1]-spring_len[0]) / m * dt >= 0 :
            t_of_largest = t
        elif ball_v[1] > 0 and ball_v[1]-k * (spring_len[1]-spring_len[0]) / m * dt <= 0:
            t_of_smallest = t
        elif t_of_largest > 0 and t_of_smallest > 0:
            T = 2 * abs(t_of_largest - t_of_smallest)
            print(T)
