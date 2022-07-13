import matplotlib.pyplot as plt

g = -9.8
u = 8
dt = 0.05
t = 0
a = g
v = u
d = 0
T = [t]
V = [v]
for counter in range(100):
    t += dt
    v += a * dt
    d += v * dt
    T.append(t)
    V.append(v)
    print(t, v, d)

plt.plot(T, V)

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('My first graph!')

# function to show the plot
plt.show()
