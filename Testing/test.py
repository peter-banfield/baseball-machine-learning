import os

filePath = os.path.join('..', 'Datasets', 'gl2010_17', 'GL2017.TXT')

with open(filePath, 'r') as f:
    lineOne = f.readline()

lineOne = lineOne.split(',')

for i in range(len(lineOne)):
    item = lineOne[i]
    if '"' not in item:
        lineOne[i] = int(item)
    else:
        lineOne[i] = item.replace('"', '')

print(lineOne)