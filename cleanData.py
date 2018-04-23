import os

def addToDict(clss, inDict, attend):
    """Input: clss = fields of interest, inDict = existing dictionary, attend = integer attendace for game
    Output: dictionary containing the new information"""
    # Case 1: new class found
    if clss not in inDict:
        inDict[clss] = (attend, 1)
    
    # Case 2: class in dict
    else:
        inDict[clss] = (inDict[clss][0] + attend, inDict[clss][1] + 1)
    
    return inDict

def avgAttend(inDict):
    """Input: dict where key = class, values = (sumAttendance, numSum)
    Output: dict where key = class, values = avg attendance"""
    for k in inDict:
        inDict[k] = inDict[k][0] / inDict[k][1]
    return inDict

def normalize(classDict): 
    """Input: classDict has dictionary with keys = class, values = average attend
    Output: list of ordered classes"""
    avgList = []
    newDict = {}
    classList = []

    for k in classDict:
        newDict[classDict[k]] = k
        avgList.append(classDict[k])

    avgList.sort()

    for avg in avgList:
        classList.append(newDict[avg])

    return classList

def normData(parkID, filePath=os.path.join('Datasets', 'Cleaned', 'CGL2017.txt')):
    """Input: parkId representing the stadium, path to data file
    Output: list of normalized class lists with first element in each list being name of list"""
    dayTimeDict = {}
    visitDict = {}
    
    with open(filePath, 'r') as data:
        
        for line in data:
            elements = line.strip().split(',')
            if elements[7] != parkID:
                continue
            
            dayTimeDict = addToDict((elements[1], elements[6]), dayTimeDict, int(elements[8]))
            visitDict = addToDict(elements[2], visitDict, int(elements[8]))

    dayTimeDict = avgAttend(dayTimeDict)
    visitDict = avgAttend(visitDict)

    dayTimeList = normalize(dayTimeDict)
    visitList = normalize(visitDict)

    dayTimeList.insert(0, 'dayTimeList')
    visitList.insert(0, 'visitList')

    masterList = [dayTimeList, visitList]    
    
    return masterList
