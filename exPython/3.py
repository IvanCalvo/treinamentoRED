import matplotlib.pyplot as plt
import numpy as np
import math

def plotPonto(x,y):
	circle1 = plt.Circle((0, 0), 1, color='b')
	circle2 = plt.Circle((x, y), 0.03, color='r')
	fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot
	ax.set(xlim=(-2, 2), ylim = (-2, 2))

	ax.add_artist(circle1)
	ax.add_artist(circle2)

	plt.show()
	
def proj(x, y, r, c1, c2):
	ang = math.atan((y - c2)/(x - c1))
	y2 = math.sin(ang)/r
	x2 = math.cos(ang)/r
	return x2,y2

x,y = proj(8,52,1,0,0)
plotPonto(x,y)