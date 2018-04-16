import os
import numpy as np 
import matplotlib.pyplot as plt

dataFilePath = os.path.join('..', 'Datasets', 'Cleaned', 'CGL2017.TXT')
clssFilePath = os.path.join('..', 'HOU03Classes.TXT')

x=[]
y=[]

dayTimeList = []
visitList = []
parkList = []

with open(clssFilePath) as f:
    dayTimeList = f.readline().strip().split(',')
    visitList = f.readline().strip().split(',')
    parkList = f.readline().strip().split(',')


with open(dataFilePath, 'r') as f:
    
    for line in f:
        l = line.split(',')

        # day+time
        if l[7] == 'HOU03':
            clss = l[1]+l[6]
            y.append(int(l[8]))
            x.append(dayTimeList.index(clss))

        # park
        # if l[7] == 'HOU03':
        # clss = l[7]
        # y.append(int(l[8]))
        # x.append(parkList.index(clss))

        #visit
        # if l[7] == 'HOU03':
        #     clss = l[2]
        #     y.append(int(l[8]))
        #     x.append(visitList.index(clss))



         


plt.xlabel('gametime')
plt.ylabel('attendance')

plt.plot(x,y, 'bo')


plt.show()


    

