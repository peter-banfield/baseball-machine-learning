import os

inFilePath = os.path.join('Datasets', 'gl2010_17', 'GL2017.TXT')
outFilePath = os.path.join('Datasets', 'Cleaned', 'CGL2017.txt')

with open(inFilePath, 'r') as rf:
    with open(outFilePath, 'w') as of:

        elmList = [0, 2, 3, 5, 6, 8, 12, 16, 17, 160]

        for line in rf:
            try:
                if line.split(',')[17] == '':
                    continue
                if int(line.split(',')[17]) == 0: 
                    continue
            except:
                print(line)
                break

            for e in elmList:
                if e == elmList[-1]:
                    of.write(line.split(',')[e].strip().replace('"', ''))
                else:
                    of.write(line.split(',')[e].replace('"', '')+',')

            of.write('\n')