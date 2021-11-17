import numpy as np
from vpython import *
A, N = 0.10, 50
size, m, k, d = 0.06, 0.1, 10.0, 0.4
Unit_K = 2 * pi/(N*d)
chart = graph(width = 1500, title = 'Phonon dispertion relationship', xtitle = 'wavevector', ytitle = 'angular frequency', background = vec(0.5,0.5,0))
c = gcurve(color = color.cyan)

S = 0 # select ball to get T

for n in range(1,25):
    Wavevector = n * Unit_K
    phase = Wavevector * arange(N) * d
    ball_pos, ball_orig, ball_v, spring_len = np.arange(N)*d + A*np.sin(phase), np.arange(N)*d, np.zeros(N), np.ones(N)*d
    t, dt = 0, 0.0003
    largest, smallest, t_of_largest, t_of_smallest, T = 0, 0, 0, 0, 0
    while True:
        t += dt
        spring_len[:-1] = ball_pos[1:] - ball_pos[:-1]
        spring_len[-1] = ball_pos[0]-ball_pos[-1] + N*d
        ball_v[1:] += k * (spring_len[1:]-spring_len[:-1]) / m * dt
        ball_v[0] += k * (spring_len[0]-spring_len[-1]) / m * dt
        ball_pos += ball_v*dt
        if ball_v[S] < 0 and ball_v[S]-k * (spring_len[S]-spring_len[S-1]) / m * dt >= 0 :
            t_of_largest = t
        elif ball_v[S] > 0 and ball_v[S]-k * (spring_len[S]-spring_len[S-1]) / m * dt <= 0:
            t_of_smallest = t
        elif t_of_largest > 0 and t_of_smallest > 0:
            T = 2 * abs(t_of_largest-t_of_smallest)
            c.plot(Wavevector,2*pi/T)
            break
