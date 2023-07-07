import os
import queue
import shutil
from typing import List


def searchAllgz(parentFolderPath, targetPath):
    folderStack: List[str] = [os.path.join(parentFolderPath, folders) for folders in os.listdir(parentFolderPath)]
    while folderStack:
        currentFile = folderStack[-1]
        folderStack.pop(-1)
        if os.path.isdir(currentFile):
            for folders in os.listdir(currentFile):
                folderStack.append(os.path.join(currentFile, folders))
            print(folderStack)
        else:
            if ".gz" in currentFile:
                filename = currentFile.split("/")[-1]
                shutil.copy(currentFile, os.path.join(targetPath, filename))


if __name__ == "__main__":
    searchAllgz("C:\\MyInstall\\PythonWorkSpace\\", "C:\\MyInstall\\PythonWorkSpace\\")
