import numpy as np
import matplotlib.pyplot as plt

def cal_sum_norm(u, v, ord = 2):
    if ord == 1:
        return np.sum(np.absolute(u+v))
    elif ord == 'inf':
        return np.amax(np.absolute(u+v))
    else:
        return (np.sum((u+v)**ord))**(1.0/ord)

def cal_norm_sum(u, v, ord = 2):
    if ord == 1:
        return np.sum(np.absolute(u)+np.absolute(v))
    elif ord == 'inf':
        return np.amax(np.absolute(u)+np.absolute(v))
    else:
        return np.sum(np.absolute(u)**ord)**(1.0/ord) + np.sum(np.absolute(v)**ord)**(1.0/ord)

def plot_one_circle(origin, r, color):
    theta_array = np.linspace(0, 2*np.pi, 500)
    x = np.asarray([origin[0]+r*np.cos(theta) for theta in theta_array])
    y = np.asarray([origin[1]+r*np.sin(theta) for theta in theta_array])
    plt.plot(x, y, color)

def plot_circle(u, v, ord):
    fig = plt.figure()
    origin = np.array([0, 0])
    plot_one_circle(origin, cal_sum_norm(u, 0, ord), 'r')
    plot_one_circle(u, cal_sum_norm(v, 0, ord), 'b')
    plot_one_circle(origin, cal_sum_norm(u, v, ord), 'g')
    plot_one_circle(origin, cal_norm_sum(u, v, ord), 'm')
    plt.arrow(0, 0, u[0]+v[0], u[1]+v[1], length_includes_head = True)
    plt.arrow(0, 0, u[0], u[1], length_includes_head = True)
    plt.arrow(u[0], u[1], (v)[0], (v)[1], length_includes_head = True)

p = np.array([1,2,5,0.5])
sum_norm = np.array([cal_sum_norm(u, v, ord_index) for ord_index in p])
norm_sum = np.array([cal_norm_sum(u, v, ord_index) for ord_index in p])

plot_circle(u, v, 1)
fig_1 = plt.gca()

plot_circle(u, v, 2)
fig_2 = plt.gca()

plot_circle(u, v, 5)
fig_3 = plt.gca()

plot_circle(u, v, 0.5)
fig_4 = plt.gca()

plt.show()