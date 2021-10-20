from vpython import *
g = vec(0,-9.8,0)
k = 150000
m = 1
distance = 0.4
radius = 0.2
L = 2

N = 2

scene = canvas(width=500, height=500, center=vec(0, -0.2, 0),background = vec(0.5,0.5,0))
ceiling = box(length=2, height=0.005, width=0.8, color=color.blue)
balls = []
springs = []
for i in range(5):
    balls.append(sphere(pos = vec(-2*distance+i*distance, -2, 0),radius = radius,color = color.red))
    if i < N:
        balls[i].pos += vec(-0.1975**0.5,0.05,0)
    springs.append(cylinder(pos = vec(-2*distance+i*distance, 0, 0),radius = 0.005,color = color.red))
    springs[i].axis = balls[i].pos - springs[i].pos
