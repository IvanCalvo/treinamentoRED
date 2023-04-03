import matplotlib.pyplot as plt

def plotPonto(x,y):
	circle1 = plt.Circle((0, 0), 1, color='b')
	circle2 = plt.Circle((x, y), 0.03, color='r')
	fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot
	ax.set(xlim=(-2, 2), ylim = (-2, 2))

	ax.add_artist(circle1)
	ax.add_artist(circle2)

	plt.show()