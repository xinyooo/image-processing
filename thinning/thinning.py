import os
import sys
from PIL import Image

def checkOne(matrixList):
    checkList = [(element//255+1)%2 for element in matrixList]
    # Center == 1?
    if checkList[4] != 1:
        return False
    # N(P)
    N = checkList.count(1)-1
    if N < 2 or N > 6:
        return False
    # T(P)
    T = 0
    if checkList[0] == 0 and checkList[1] == 1:
        T += 1
    if checkList[1] == 0 and checkList[2] == 1:
        T += 1
    if checkList[2] == 0 and checkList[5] == 1:
        T += 1
    if checkList[5] == 0 and checkList[8] == 1:
        T += 1
    if checkList[8] == 0 and checkList[7] == 1:
        T += 1
    if checkList[7] == 0 and checkList[6] == 1:
        T += 1
    if checkList[6] == 0 and checkList[3] == 1:
        T += 1
    if checkList[3] == 0 and checkList[0] == 1:
        T += 1
    if T != 1:
        return False
    # Thinning 1
    if checkList[1]*checkList[5]*checkList[7] != 0:
        return False
    if checkList[1]*checkList[3]*checkList[5] != 0:
        return False
    return True

def checkTwo(matrixList):
    checkList = [(element//255+1)%2 for element in matrixList]
    # Center == 1?
    if checkList[4] != 1:
        return False
    # N(P)
    N = checkList.count(1)-1
    if N < 2 or N > 6:
        return False
    # T(P)
    T = 0
    if checkList[0] == 0 and checkList[1] == 1:
        T += 1
    if checkList[1] == 0 and checkList[2] == 1:
        T += 1
    if checkList[2] == 0 and checkList[5] == 1:
        T += 1
    if checkList[5] == 0 and checkList[8] == 1:
        T += 1
    if checkList[8] == 0 and checkList[7] == 1:
        T += 1
    if checkList[7] == 0 and checkList[6] == 1:
        T += 1
    if checkList[6] == 0 and checkList[3] == 1:
        T += 1
    if checkList[3] == 0 and checkList[0] == 1:
        T += 1
    if T != 1:
        return False
    # Thinning 2
    if checkList[3]*checkList[5]*checkList[7] != 0:
        return False
    if checkList[1]*checkList[3]*checkList[7] != 0:
        return False
    return True

def modifyImage(pixelMap, imgMode, imgSize):
    loop = True
    while loop:
        loop = False
        for i in range(imgSize[0]-2):
            for j in range(imgSize[1]-2):
                matrixList = [pixelMap[i, j], pixelMap[i, j+1], pixelMap[i, j+2], pixelMap[i+1, j], pixelMap[i+1, j+1], pixelMap[i+1, j+2], pixelMap[i+2, j], pixelMap[i+2, j+1], pixelMap[i+2, j+2]]
                checkReplace = checkOne(matrixList)
                if checkReplace:
                    pixelMap[i+1, j+1] = 255
                    loop = True
        for i in range(imgSize[0]-2):
            for j in range(imgSize[1]-2):
                matrixList = [pixelMap[i, j], pixelMap[i, j+1], pixelMap[i, j+2], pixelMap[i+1, j], pixelMap[i+1, j+1], pixelMap[i+1, j+2], pixelMap[i+2, j], pixelMap[i+2, j+1], pixelMap[i+2, j+2]]
                checkReplace = checkTwo(matrixList)
                if checkReplace:
                    pixelMap[i+1, j+1] = 255
                    loop = True

if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1].split('.')[0]
        image = Image.open(sys.argv[1])
        image = image.convert('1')
        modifyImage(image.load(), image.mode, image.size)
        image.save(filename+'_thinning.jpg')
    else:
        print('Need one argument for image\'s path')