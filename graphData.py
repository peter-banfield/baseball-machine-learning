import os
import numpy as np 
import matplotlib.pyplot as plt
from cleanData import normPark
# for 3d plotting
# from mpl_toolkits.mplot3d import Axes3D
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

parkID = 'PHI13'

MasterList = normPark(parkID)

# masterList = [dayTimeList, visitList]    
classDict = {}
for l in MasterList:
    k = l.pop(0)
    classDict[k] = l


dataPath = os.path.join('Datasets', 'Cleaned', 'CGL2017.txt')

x = []
y = []
z = []

with open(dataPath, 'r') as data:
    for line in data:
        l = line.strip().split(',')

        try:
            if parkID == l[7]:
                y.append(int(l[8]))
                # # time+day
                # x.append(classDict['dayTimeList'].index((l[1],l[6])))
                # visit
                x.append(classDict['visitList'].index(l[2]))
                # # win% home
                # x.append(float(l[17]))
                # # 3d x=win% y=gamenum z=attendance
                # x.append(float(l[17]))
                # y.append(int(l[5]))
                # z.append(int(l[8]))
        except:
            print(line, classList)
            exit()

# Axes3D.scatter(ax,x,y,zs=z)
plt.plot(x,y, 'bo')
plt.show()
