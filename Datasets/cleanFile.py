import os

inFilePath = os.path.join('gl2010_17', 'GL2017.TXT')
outFilePath = os.path.join('Cleaned', 'CGL2017.txt')
with open(inFilePath, 'r') as rf:
    with open(outFilePath, 'w') as of:

        elmList = [0, 2, 3, 5, 6, 8, 12, 16, 17, 160, 1, 13, 14, 15, 9, 10]

        teamDict = {}
        for line in rf:
            l = line.strip().split(",")            
            for e in elmList:
                
                if l[17] == "":
                   pass 
                elif e == elmList[-1] and e != 10:
                    of.write(l[e].replace('"', ''))
                else:
                    of.write(l[e].replace('"', '')+',')
                if e == 10:#find win percent
                    if l[6] not in teamDict:
                        teamDict[l[6]] = [0,0]
                    if l[3] not in teamDict:
                        teamDict[l[3]] = [0,0]
                    if int(l[10]) > int(l[9]):
                        teamDict[l[6]][0] += 1
                    elif int(l[10]) < int(l[9]):
                        teamDict[l[3]][0] += 1
                    else:
                        teamDict[l[6]][0] += .5
                        teamDict[l[3]][0] += .5
                    teamDict[l[6]][1] += 1
                    teamDict[l[3]][1] += 1

                    hteamwp = round(teamDict[l[6]][0]/teamDict[l[6]][1], 3)
                    vteamwp = round(teamDict[l[3]][0]/teamDict[l[3]][1], 3)
                    if l[17] != "":
                        of.write(str(vteamwp)+","+str(hteamwp))
                        if e != elmList[-1]:
                            of.write(",")

            of.write('\n')

