import numpy as np
import math
from matplotlib import pyplot as plt
from matplotlib import animation
from hopf import *

fig = plt.figure()
ax = plt.axes(xlim=(XMIN, XMAX), ylim=(0,10))
line, = ax.plot([], [], lw=2)

def init():
	line.set_data([],[])
	return line,

def animate(i):
	global u
	for i in range(3): 
		u = update(u)
	line.set_data(XVALUES, u)
	return line,

u = initial()

anim = animation.FuncAnimation(fig, animate, 
		init_func=init, frames=500, interval=25, blit=True, repeat=False)
anim.save('hopf_animation.mp4', writer='mencoder', fps=40)
