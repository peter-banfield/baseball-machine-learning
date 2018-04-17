import os
import numpy as np 
import matplotlib.pyplot as plt
from cleanData import normPark

parkID = 'CHI11'

MasterList = normPark(parkID)

classList = MasterList[1][1:]

dataPath = os.path.join('Datasets', 'Cleaned', 'CGL2017.txt')

x = []
y = []

with open(dataPath, 'r') as data:
    for line in data:
        l = line.strip().split(',')

        if parkID == l[7]:
            y.append(int(l[8]))
            # time+day
            # x.append(classList.index((l[1],l[6])))
            # visit
            # x.append(classList.index(l[2]))

plt.plot(x,y, 'bo')
plt.show()
