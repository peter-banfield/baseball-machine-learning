import os
import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def subPlot2D(X, Y, weights):
    fig, (sp1, sp2) = plt.subplots(1,2)
    
    sp1x = [i[1] for i in X]
    sp1.plot(sp1x, Y, 'bo')
    xmin = min(sp1x) 
    xmax = max(sp1x)
    x = [j for j in range(int(xmin),int(xmax)+1)]
    y = [weights[0][0]+weights[1][0] * e for e in x]
    sp1.plot(x,y)
    sp1.set_title('Attendence vs Day+Time')

    sp2x = [i[2] for i in X]
    sp2.plot(sp2x, Y, 'bo')
    xmin = min(sp2x) 
    xmax = max(sp2x)
    x = [j for j in range(int(xmin),int(xmax)+1)]
    y = [weights[0][0]+weights[2][0] * e for e in x]
    sp2.plot(x,y)
    sp2.set_title('Attendence vs Away Team')

    
    plt.show()

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

def threeDPlot(x, z, weights):
    
    gx = [i[1] for i in x]
    gy = [i[2] for i in x]
    xmin = min(gx) 
    xmax = max(gx)
    ymin = min(gy) 
    ymax = max(gy)


    x = np.arange(xmin, xmax, 1)
    y = np.arange(ymin, ymax, 1)

    X, Y = np.meshgrid(x, y)

    Z = weights[0][0] + weights[1][0] * X + weights[2][0] * Y

   
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    az = np.array(z)
    agx = np.array(gx)
    agy = np.array(gy)
    ax.scatter(agx,agy,az, c='r')
    ax.plot_wireframe(X,Y,Z)

    ax.set_xlabel('Day+Time')
    ax.set_ylabel('Away Team')
    ax.set_zlabel('Attendance')

    plt.show()