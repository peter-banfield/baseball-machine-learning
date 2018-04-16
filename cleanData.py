import os

filePath = os.path.join('Datasets', 'Cleaned', 'CGL2017.txt')

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

# key = class, element = (sumAttend, numSum)
dayTimeDict = {}
visitDict = {}
parkDict = {}

with open(filePath, 'r') as inFile:

    for line in inFile:
        elements = line.split(',')

        # Case 1: new day+time class found
        if (elements[1], elements[6]) not in dayTimeDict:
            dayTimeDict[(elements[1], elements[6])] = (int(elements[8]), 1)
        
        # Case 2: day+night class in dict
        else:
            dayTimeDict[(elements[1], elements[6])] = (dayTimeDict[(elements[1], elements[6])][0]+int(elements[8]), dayTimeDict[(elements[1], elements[6])][1]+1)

        # Case 1: new visit class found
        if elements[2] not in visitDict:
            visitDict[elements[2]] = (int(elements[8]), 1)
        
        # Case 2: visit class in dict
        else:
            visitDict[elements[2]] = (visitDict[elements[2]][0] + int(elements[8]), visitDict[elements[2]][1] + 1)
        
        # Case 1: new park class found
        if elements[7] not in parkDict:
            parkDict[elements[7]] = (int(elements[8]), 1)
        
        # Case 2: park class in dict
        else:
            parkDict[elements[7]] = (parkDict[elements[7]][0] + int(elements[8]), parkDict[elements[7]][1] + 1)

dayTimeList = normalize(dayTimeDict)
visitList = normalize(visitDict)
parkList = normalize(parkDict)

outFilePath = os.path.join('normalizedClasses.txt')
listNorm = [dayTimeList, visitList, parkList]

with open(outFilePath, 'w') as outFile:
    for l in listNorm:
        for clss in l:
            if clss == l[-1]:
                outFile.write(str(clss)+'\n')
            else:
                outFile.write(str(clss)+',')