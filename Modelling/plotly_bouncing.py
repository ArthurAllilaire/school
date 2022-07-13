import plotly.express as px

g = -9.8
u = 8
dt = 0.05
t = 0
a = g
v = u
d = 0
bounciness = -0.9
# Between 0 and -infinity - -2 = trampoline
T = [t]
V = [v]
D = [d]
for counter in range(200):
    t += dt
    v += a * dt
    if (d + v * dt) < 0:
        d = 0
        v *= bounciness
    else:
        d += v * dt
    T.append(t)
    V.append(v)
    D.append(d)

fig = px.scatter(x=T, y=D)
fig.show()
