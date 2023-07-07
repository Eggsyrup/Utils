import cv2
import os
import numpy as np
import csv

from tqdm import tqdm


# 从EXCEL中找到特定的器官
def findSpeOrgan(deepLesionPath, organID):
    csvPath = os.path.join(deepLesionPath, "DL_info.csv")
    imagePath = []
    lNu = []
    with open(csvPath, "r", encoding='UTF-8') as csvFile:
        reader = csv.reader(csvFile)
        for row in tqdm(reader):
            if row[9] == str(organID):
                start = row[11].split(", ")[0]
                end = row[11].split(", ")[1]
                indexRange = range(int(start), int(end) + 1)
                folder = row[0].rsplit("_", 1)[0]
                for i in indexRange:
                    path = os.path.join(folder, "{}.png".format(i))
                    if path not in imagePath:
                        imagePath.append(path)
                        upper = row[14].split(", ")[1]
                        lower = row[14].split(", ")[0]
                        lNu.append([float(lower), float(upper)])
    return imagePath, lNu


def resizeAndResetUnit(deepLesionPath, targetPath, organID):
    """
        read Hounsfield Window size from CSV file if there is one.
        For example, if the min and max values of a window is A and B, then the windowed intensity I should be
                I = min(255, max(0, (HU-A)/(B-A)*255);
    """
    imagePaths, lNu = findSpeOrgan(deepLesionPath, organID)
    i = 0
    nameCounter = 0
    for imagePath in tqdm(imagePaths):
        image = cv2.imread(os.path.join(deepLesionPath, imagePath), cv2.IMREAD_UNCHANGED)
        i += 1
        if image is None or image.shape != (512, 512):
            continue
        image = image.astype(float) - 32768
        image = (image - lNu[i][0]) / (lNu[i][1] - lNu[i][0]) * 255
        image = cv2.pyrDown(image)
        cv2.imwrite(os.path.join(targetPath, "{}.png".format(nameCounter)), image)
        nameCounter += 1


def tempModify():
    path = os.path.join(r"../DataSet/deeplesion/train")
    lower = -1024  # default B of other Image_png dataset
    upper = 3071  # default A as well
    file_list = os.listdir(path)
    for file in tqdm.tqdm(file_list):
        filepath = os.path.join(path, file)
        fullName = path + "_" + file
        image = cv2.imread(filepath, cv2.CV_16UC1).astype(np.int32, copy=False)

        # for row in reader:
        #     if row[0] == fullName:
        #         window = row[14]
        #         break
        # window = window.split(",")
        # lower = window[0][1:]
        # upper = window[1][0:-1]
        if image.shape != (256, 256):
            hight = image.shape[0]
            width = image.shape[1]
            hight_start = int((hight - 256) / 2 - 1)
            hight_end = int(hight - (hight - 256) / 2) - 1
            width_start = int((width - 256) / 2) - 1
            width_end = int(width - (width - 256) / 2) - 1
            image = image[hight_start:hight_end][width_start:width_end]
        cv2.imwrite(os.path.join(filepath), image)


def filter():
    path = os.path.join(r"../DataSet/deeplesion/valid")
    lower = -1024  # default B of other Image_png dataset
    upper = 3071  # default A as well
    file_list = os.listdir(path)
    for file in tqdm.tqdm(file_list):
        filepath = os.path.join(path, file)
        image = cv2.imread(filepath, cv2.CV_16UC1).astype(np.int32, copy=False)
        if image.shape != (256, 256):
            os.remove(filepath)


if __name__ == "__main__":
    resizeAndResetUnit("D:\\imageData\\DeepLesion\\Images_png\\", "D:\\imageData\\DeepLesion\\origin\\", 3)
