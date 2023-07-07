import os


def rename(folder_path):
    name_list = os.listdir(os.path.join(folder_path))
    for i, name in enumerate(name_list):
        ext = name.split(".")[-1]
        os.rename(os.path.join(folder_path, name), os.path.join(folder_path, str(i).zfill(12))+"."+ext)


if __name__ == "__main__":
    rename(r"C:\MyInstall\PythonWorkSpace\DPIR-master\dataset\test\gt_imgs")
