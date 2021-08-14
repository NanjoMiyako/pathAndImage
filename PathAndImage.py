import sys
import random


def delKaigyo(line):
    return line.replace('\n','')

args = sys.argv

    
def getImageURLByPosIdx(pathName):
    for l1 in Lines1:
        l2 = l1.split(',')
        if pathName == l2[0]:
            return l2[1]
    return l2[1]

def getNextRndPath(currentPos, prevPos):
    for l1 in Lines2:
        l2 = l1.split(',')
        if currentPos == l2[0]:
            for j in range(10):
                rIdx = random.randint(1, (len(l2)-1))
                if l2[rIdx] != prevPos:
                    return l2[rIdx]
            
    
    return l2[1]
    

print(len(sys.argv))

if len(args) < 5:
 exit()

ImageAndPathNameFile = args[1];
file1 = open(ImageAndPathNameFile, 'r')
#PathMapFile
PathMapFile = args[2]
file2 = open(PathMapFile, 'r')

outputF = open(args[3], 'w')

MoveLen = int(args[4])


Lines1 = file1.readlines()
Lines1 = list(map(delKaigyo, Lines1))

Lines2 = file2.readlines()
Lines2 = list(map(delKaigyo, Lines2))

print(Lines1)
print(Lines2)

PathList = [];


prevPos = Lines1[0].split(',')[0]
currentPos = Lines1[0].split(',')[0]
outputF.write(getImageURLByPosIdx(prevPos))
outputF.write('\n')
for i in range(MoveLen):
    newPos = getNextRndPath(currentPos, prevPos)
    outputF.write(getImageURLByPosIdx(newPos))
    outputF.write('\n')
    prevPos = currentPos
    currentPos = newPos

outputF.close()

    