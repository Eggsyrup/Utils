import os

import cv2
from cv2 import dnn_superres


def superResolution():
    img_path = os.path.join("..", "DIP", "dataset", "output")
    imgList = os.listdir(img_path)
    modelPath = os.path.join("ESPCN_x2.pb")
    sr = dnn_superres.DnnSuperResImpl_create()
    sr.readModel(modelPath)
    sr.setModel("espcn", 2)
    for img_name in imgList:
        img = cv2.imread(os.path.join(img_path, img_name))
        img = sr.upsample(img)
        cv2.imwrite(os.path.join(img_path, img_name), img)


if __name__ == "__main__":
    superResolution()
