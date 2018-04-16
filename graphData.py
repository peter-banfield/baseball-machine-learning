import os
import numpy as np 
import matplotlib.pyplot as plt
from cleanData import normPark

parkID = 'HOU03'

MasterList = normPark(parkID)

classList = MasterList[0][1:]

dataPath = os.path.join('Datasets', 'Cleaned', 'CGL2017.txt')

x = []
y = []

with open(dataPath, 'r') as data:
    for line in data:
        l = line.strip().split(',')

        if parkID == l[7]:
            y.append(int(l[8]))
            # x.append(classList.index((l[1],l[6])))
            x.append(int(l[5]))

plt.plot(x,y, 'bo')
plt.show()
