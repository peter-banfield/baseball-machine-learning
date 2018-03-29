import os

filePath = os.path.join('..', 'Datasets', 'gl2010_17', 'GL2017.TXT')

with open(filePath, 'r') as f:
    lineOne = f.readline()

lineOneList = lineOne.split(',')

for i in range(len(lineOneList)):
    item = lineOneList[i]
    if '"' not in item:
        lineOneList[i] = int(item)
    else:
        lineOneList[i] = item.replace('"', '')

print(lineOneList)