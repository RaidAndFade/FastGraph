import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
import math

import random

style.use('fivethirtyeight')

fig, ax = plt.subplots()
ln, = plt.plot([], [], 'ro')
xdata, ydata = [], []

def init():
    ax.set_xlim(0, 20*np.pi)
    ax.set_ylim(-10, 10)
    from threading import Thread
    adder = Thread(target=adderthread)
    adder.start()
    return ln,

def adderthread():
    import time
    i=0
    while True:
        st = time.time()
        print(i/100)
        xdata.append(i/100)
        ydata.append(math.sin(i/100))
        i+=1
        time.sleep(max(0,0.001-(time.time()-st)))

def animate(i):
    ln.set_data(xdata, ydata)
    return ln,

ani = animation.FuncAnimation(fig, animate, interval=100, init_func=init,)
plt.show()