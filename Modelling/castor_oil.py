import math
import plotly.express as px

# CONSTANTS
g = -9.8
dt = 0.01
t = 0
u = 0
v = u
# CONSTANT VARS
vis = 0.95
r = 5*10**(-3)
d_ball = 7800  # kg/m^3
b_mass = d_ball * (4/3) * math.pi*r**3
# Dropped from top
# How far from start of oil is the band
# h_b_bottom = 0.1
# h_b_top = 0.4
h_oil = 0.8
h_ball = 1.5
# Need initial acceleration, velocity and distance @t=0
a = g

T = [t]
V = [v]
D = [h_ball]
A = [a]
while True:
    t += dt
    if h_ball <= h_oil:
        # - sign reverses the velocity (always an opposing force)
        drag_force = -6*math.pi*r*vis*v
    else:
        drag_force = 0
    a = g + drag_force/b_mass
    v += a * dt
    # The only reason the ball would go up is if the time increment was too large and so drag_force is too large as uses a v that's too high
    if v > 0:
        v = 0
    h_ball += v * dt
    T.append(t)
    V.append(v)
    D.append(h_ball)
    A.append(a)
    if h_ball < 0:
        break
fig = px.scatter(x=T, y=D)
fig.show()
