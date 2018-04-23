import os

inFilePath = os.path.join('..','Datasets','Cleaned', 'CGL2017.txt')

with open(inFilePath, 'r') as inFile:
    for line in inFile:
        elements = line.strip().split(',')

        if elements[8] == '0' or elements[8] == '':
            print(line)