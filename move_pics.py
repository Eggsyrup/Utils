import os
import shutil

import tqdm


def move_pic(src_folder_path="D:/DATA/dataset", target_folder_path="", start_num=0, end_num=0):
    global_counter = 50

    sub_folder_list = os.listdir(os.path.join(src_folder_path))

    if sub_folder_list is None:
        Exception("The src folder is empty")
    # if len(name_list) > start_num:
    #     Exception("Pic Num Error, Num Index Out Of Boundary")
    try:
        if len(os.listdir(os.path.join(target_folder_path))) > 0:
            print("The Target Folder is not Empty. Do you want to clear the folder first?[Y/N]")
            choice = input()
            if choice in ["Yes", "y", "yes", "Y"]:
                shutil.rmtree(os.path.join(target_folder_path))
                print("The target folder is clear now")
                os.mkdir(os.path.join(target_folder_path))
    except FileNotFoundError:
        os.mkdir(os.path.join(target_folder_path))
    for folder_name in tqdm.tqdm(sub_folder_list):
        name_list = os.listdir(os.path.join(src_folder_path, folder_name))
        # for name in name_list[start_num:end_num]:
        #     shutil.copy(os.path.join(src_folder_path, folder_name, name), os.path.join(target_folder_path, name))
        for name in name_list:
            shutil.copy(os.path.join(src_folder_path, folder_name, name), os.path.join(target_folder_path, str(global_counter)+".png"))
            global_counter -= 1
            if global_counter < 0: return


if __name__ == "__main__":
    move_pic(r"D:\imageData\DeepLesion\Images_png", r"C:\MyInstall\PythonWorkSpace\PoissonDenoiser\DataSet\test")
