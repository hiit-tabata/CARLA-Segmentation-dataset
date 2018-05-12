from os import listdir, remove
from os.path import isfile, join


RGB_FOLDER_NAME = '../dataset/rgb'
SEGMENTATION_FOLDER_NAME = '../dataset/segmentation'
DEPTH = '../dataset/depth'

def removeFiles(a, b, c):
    rgbFiles = [f for f in listdir(a) if isfile(join(a, f))]
    for f in rgbFiles:
        if not isfile(join(b, f)) or not isfile(join(c, f)):
            if isfile(join(b, f)):
                remove(join(b, f))
            if isfile(join(c, f)):
                remove(join(c, f))

            remove(join(a, f))

removeFiles(RGB_FOLDER_NAME, SEGMENTATION_FOLDER_NAME, DEPTH)
removeFiles(SEGMENTATION_FOLDER_NAME, DEPTH, RGB_FOLDER_NAME)
removeFiles(DEPTH, RGB_FOLDER_NAME, SEGMENTATION_FOLDER_NAME)

# print(rgbFiles)