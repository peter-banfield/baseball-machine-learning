import os
import numpy as np 
import matplotlib.pyplot as plt
from cleanData import normPark
from linearRegression import regress, getValue
from graphData import twoDPlot, threeDPlot
from UI import setup, error, checkValues, getValues, makeButton, makeOutput

def teamToPark(teamID):
    filename = os.path.join('Datasets', "teamPark.txt")
    with open(filename, 'r') as file:
        for line in file:
            e = line.strip().split(",")
            if e[0] == teamID:
                return e[1]

def getParkName(parkID):
    filename = os.path.join('Datasets', "parkCode.txt")
    with open(filename, 'r') as file:
        for line in file:
            e = line.strip().split(",")
            if e[0] == parkID:
                return e[1]

def doRegression(valList):
    parkID = teamToPark(valList[0])
    dataPath = os.path.join('Datasets', 'Cleaned', 'CGL2017.txt')
    MasterList = normPark(parkID)
  
    classDict = {}
    for l in MasterList:
        k = l.pop(0)
        classDict[k] = l

    X = []
    Y = []
    with open(dataPath, 'r') as data:
        for line in data:
            l = line.strip().split(',')


            if parkID == l[7]:
                Y.append(int(l[8]))
                X.append([1, classDict['dayTimeList'].index((l[1],l[6])), classDict['visitList'].index(l[2])])


    w = regress(X, Y)

    result = getValue(w, x)


    return result, w, getParkName(parkID)



def main():
    
    root, window, objects, choices, teamDict = setup()

    #When button is pressed
    def buttonClicked(*args):
        values = getValues(objects)
        if checkValues(values,choices):
            error(window)
            return

        valList = [teamDict[values[0]], teamDict[values[1]], (values[2][:3],values[3][:1])]
        root.destroy()
        result, weights, parkName = doRegression(valList)
        makeOutput(values, result, weights, parkName)


    #create button to confirm answers
    makeButton(window, buttonClicked)
    root.mainloop()

main()




    # with open(dataPath, 'r') as data:
    #     for line in data:
    #         l = line.strip().split(',')


    #         if parkID == l[7]:
    #             y.append(int(l[8]))
    #             # # time+day
    #             # x.append([1,classDict['dayTimeList'].index((l[1],l[6]))])
    #             # visit
    #             x.append([1,classDict['visitList'].index(l[2])])
    #             # x.append([1,classDict['dayTimeList'].index((l[1],l[6])),classDict['visitList'].index(l[2])])

    # w = regress(x, y)
    # gx = [i[1] for i in x]
    # # gy = [i[2] for i in x]
    # # print(w)
    # twoDPlot(gx,y,w)
    # # threeDPlot(gx,gy,y,w)