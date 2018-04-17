import os
import numpy as np 
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D

#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')

dataFilePath = os.path.join('..', 'Datasets', 'Cleaned', 'CGL2017.TXT')
clssFilePath = os.path.join('..', 'normalizedClasses.TXT')

x=[]
y=[]
# z=[]

daylist = ['Mon', 'Tue', "Wed", 'Thu', 'Fri', 'Sat','Sun']
teamList = [0, ]

with open(filePath, 'r') as f:
    
    for lineOne in f:
        

        #clean data
        lineOneList = lineOne.split(',')
        for i in range(len(lineOneList)):
            item = lineOneList[i]
            lineOneList[i] = item.replace('"', '')
        
        
        #plot at-bats v hit v homeruns
        # x.append(int(lineOneList[21])) #at bat
        # y.append(int(lineOneList[22])) #hit
        # z.append(int(lineOneList[25])) #homerun
        

        # x.append(int(lineOneList[49]))
        # y.append(int(lineOneList[50]))
        # z.append(int(lineOneList[53]))

        #if lineOneList[16] == 'PHO01':
            day = lineOneList[2]
            nd = lineOneList[12]
            attend = lineOneList[17]

            if nd == 'D':
                dayMod = daylist.index(day)*2
            else:
                dayMod = daylist.index(day)*2+1

            x.append(dayMod)
            y.append(int(attend))


         
# Axes3D.scatter(ax,x,y,zs=z)
# plt.xlabel("at bat")
# plt.ylabel('hit')

plt.xlabel('gametime')
plt.ylabel('attendance')

plt.plot(x,y, 'bo')


plt.show()


    

