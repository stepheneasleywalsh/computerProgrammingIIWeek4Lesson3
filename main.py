import time
import matplotlib.pyplot as p
import math as m

p.ion()

xValues = []
yValues = []

theta = 0
while theta <= 2.1*m.pi:
    p.clf()
    xValues.append(m.cos(theta))
    yValues.append(m.sin(theta))
    p.title("The Unit Circle")
    p.axhline()
    p.axvline()
    ax = p.gca()
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    p.plot(xValues,yValues,color="red")
    p.draw()
    p.pause(0.1)
    theta += 0.1

time.sleep(1)
quit()