import os
import numpy as np 
import matplotlib.pyplot as plt
from cleanData import normPark
from linearRegression import regress
from graphData import twoDPlot, threeDPlot

parkID = 'HOU03'
dataPath = os.path.join('Datasets', 'Cleaned', 'CGL2017.txt')
MasterList = normPark(parkID)

# masterList = [dayTimeList, visitList]    
classDict = {}
for l in MasterList:
    k = l.pop(0)
    classDict[k] = l

x = []
y = []

with open(dataPath, 'r') as data:
    for line in data:
        l = line.strip().split(',')


        if parkID == l[7]:
            y.append(int(l[8]))
            # # time+day
            # x.append([1,classDict['dayTimeList'].index((l[1],l[6]))])
            # visit
            x.append([1,classDict['visitList'].index(l[2])])
            # x.append([1,classDict['dayTimeList'].index((l[1],l[6])),classDict['visitList'].index(l[2])])

w = regress(x, y)
gx = [i[1] for i in x]
# gy = [i[2] for i in x]
# print(w)
twoDPlot(gx,y,w)
# threeDPlot(gx,gy,y,w)

