import os
import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



def twoDPlot(x, y, weights):
    plt.plot(x,y, 'bo')
    xmin = min(x) 
    xmax = max(x)
    # X = np.linspace(xmin, xmax, num=10)
    X = [j for j in range(int(xmin),int(xmax)+1)]
    # Y = np.multiply(weights[0][0], X).transpose()
    Y = [weights[0][0]+weights[1][0] * e for e in X]
    plt.plot(X, Y)
    plt.show()

def threeDPlot(x, y, z, weights):
    xmin = min(x) 
    xmax = max(x)
    ymin = min(y) 
    ymax = max(y)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    Axes3D.scatter(ax,x,y)
    X = np.linspace(xmin,xmax).tolist()
    Y = np.linspace(ymin,ymax).tolist()
    Z = []
    for i in range(len(X)):
        Z.append(weights[0][0] + weights[1][0] * X[i] + weights[2][0] * Y[i])

    Axes3D.plot_surface(X,Y,Z)