from vpython import *
g = vec(0,-9.8,0)
k = 150000
m = 1
distance = 0.4
radius = 0.2
L = 2

N = 3

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
    balls[i].v = vec(0,0,0)

def af_col_v(m1, m2, v1, v2, x1, x2):
    v1_prime = v1 + 2*(m2/(m1+m2))*(x1-x2) * dot (v2-v1, x1-x2) / dot (x1-x2, x1-x2)
    v2_prime = v2 + 2*(m1/(m1+m2))*(x2-x1) * dot (v1-v2, x2-x1) / dot (x2-x1, x2-x1)
    return (v1_prime, v2_prime)

dt = 0.0001
while True:
    rate(500)
    for i in range(5):
        springs[i].axis = balls[i].pos - springs[i].pos
        spring_force = -k*(mag(springs[i].axis)-L)*springs[i].axis.norm()
        balls[i].a = g + spring_force/m
        balls[i].v += balls[i].a*dt
        balls[i].pos += balls[i].v*dt

    for i in range(4):
        if (mag(balls[i].pos - balls[i+1].pos) <= radius*2 and dot(balls[i].pos-balls[i+1].pos, balls[i].v-balls[i+1].v) <= 0) :
            (balls[i].v, balls[i+1].v) = af_col_v (m, m, balls[i].v, balls[i+1].v, balls[i].pos, balls[i+1].pos)
        
