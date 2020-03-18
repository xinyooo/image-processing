import os
import sys
from PIL import Image

def filter3x3(matrixList):
    checkList = [(element//255+1)%2 for element in matrixList]
    if checkList[4] == 1:
        N = checkList.count(1)-1
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
        # Thinning 1
        if N >= 2 and N <= 6 and T == 1 and checkList[1]*checkList[5]*checkList[7] == 0 and checkList[1]*checkList[3]*checkList[5] == 0:
            matrixList[4] = 255
        # Thinning 2
        if N >= 2 and N <= 6 and T == 1 and checkList[3]*checkList[5]*checkList[7] == 0 and checkList[1]*checkList[3]*checkList[7] == 0:
            matrixList[4] = 255
        return matrixList
    else:
        return matrixList
def modifyImage(pixelMap, imgMode, imgSize):
    for i in range(imgSize[0]-2):
        for j in range(imgSize[1]-2):
            matrixList = [pixelMap[i, j], pixelMap[i, j+1], pixelMap[i, j+2], pixelMap[i+1, j], pixelMap[i+1, j+1], pixelMap[i+1, j+2], pixelMap[i+2, j], pixelMap[i+2, j+1], pixelMap[i+2, j+2]]
            newMatrixList = filter3x3(matrixList)
            pixelMap[i, j] = newMatrixList[0]
            pixelMap[i, j+1] = newMatrixList[1]
            pixelMap[i, j+2] = newMatrixList[2]
            pixelMap[i+1, j] = newMatrixList[3]
            pixelMap[i+1, j+1] = newMatrixList[4]
            pixelMap[i+1, j+2] = newMatrixList[5]
            pixelMap[i+2, j] = newMatrixList[6]
            pixelMap[i+2, j+1] = newMatrixList[7]
            pixelMap[i+2, j+2] = newMatrixList[8]

if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1].split('.')[0]
        image = Image.open(sys.argv[1])
        image = image.convert('1')
        modifyImage(image.load(), image.mode, image.size)
        image.save(filename+'_thinning.jpg')
    else:
        print('Need one argument for image\'s path')