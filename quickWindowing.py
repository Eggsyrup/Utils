import cv2
import numpy as np


def quickWindowing(imgPath):
    image = cv2.imread(imgPath, cv2.IMREAD_UNCHANGED).astype(float) - 32768
    upper = 275
    lower = -175
    image = (image - lower) / (upper - lower) * 255
    cv2.imwrite("direct_result.png", image)
    cv2.imwrite("unit8_result.png", image.astype("uint8"))


if __name__ == "__main__":
    quickWindowing("023.png")
