import os
import numpy as np 
import matplotlib.pyplot as plt
from cleanData import normPark
from linearRegression import regress, getValue
from graphData import subPlot2D, threeDPlot
from UI import setup, error, checkValues, getValues, makeButton, makeOutput, dataError

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
    
    if valList[2] not in classDict['dayTimeList']:
        return 0
    if valList[1] not in classDict['visitList']:
        return 1

    X = []
    Y = []
    with open(dataPath, 'r') as data:
        for line in data:
            l = line.strip().split(',')


            if parkID == l[7]:
                Y.append(int(l[8]))
                X.append([1, classDict['dayTimeList'].index((l[1],l[6])), classDict['visitList'].index(l[2])])


    w = regress(X, Y)
    xValues = [1]
    xValues.append(classDict['dayTimeList'].index(valList[2]))
    xValues.append(classDict['visitList'].index(valList[1])) 
    result = getValue(w, xValues)

    return result, w, getParkName(parkID), X, Y

def main():
    
    root, window, objects, choices, teamDict = setup()

    #When button is pressed
    def buttonClicked(*args):
        values = getValues(objects)
        if checkValues(values,choices):
            error(window)
            return None

        valList = [teamDict[values[0]], teamDict[values[1]], (values[2][:3],values[3][:1])]
        root.destroy()
        regressed = doRegression(valList)
        if regressed == 0 or regressed == 1:
            dataError(values, regressed)
            return None
        else:
            result, weights, parkName, X, Y = regressed
        makeOutput(values, result, weights, parkName)
        threeDPlot(X, Y, weights) 
        subPlot2D(X, Y, weights)


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