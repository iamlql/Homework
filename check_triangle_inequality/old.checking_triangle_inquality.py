import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge, CirclePolygon

def sum_norm(u, v, ord = 2):
	if ord == 1:
		return np.sum(np.absolute(u+v))
	elif ord == 'inf':
		return np.amax(np.absolute(u+v))
	else:
		return (np.sum((u+v)**ord))**(1.0/ord)

def norm_sum(u, v, ord = 2):
	if ord == 1:
		return np.sum(np.absolute(u)+np.absolute(v))
	elif ord == 'inf':
		return np.amax(np.absolute(u)+np.absolute(v))
	else:
		return np.sum(u**ord)**(1.0/ord) + np.sum(v**ord)**(1.0/ord)

def plot_circle(u, v, ord):
	x = np.array([0,0])
	fig = plt.figure()
	fig.add_subplot(111)

	plt.gca().add_patch(CirclePolygon(x, sum_norm(u,0, ord), fill = False, resolution = 500, color = 'r'))
	plt.gca().add_patch(CirclePolygon(x, sum_norm(v,0, ord), fill = False, resolution = 500, color = 'b'))
	plt.gca().add_patch(CirclePolygon(x, sum_norm(u,v, ord), fill = False, resolution = 500, color = 'g'))
	plt.gca().add_patch(CirclePolygon(x, norm_sum(u,v, ord), fill = False, resolution = 500, color = 'm'))
	plt.arrow(0, 0, u[0], u[1], length_includes_head = True)
	plt.arrow(u[0], u[1], (v)[0], (v)[1], length_includes_head = True, )
	plt.axis('equal')
	plt.axis('off')
	


if __name__ == "__main__":
	u = np.array([1,2])
	v = np.array([2,2])
	for p in [1, 2, 5, 0.5]:
		plot_circle(u,v, p)
	plt.show()
