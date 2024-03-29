import os
import sys


# verifications
def check_input_folder_exists(
    folder_path: str
) -> None:
    if not os.path.exists(folder_path):
        raise Exception(f"[{folder_path}] does not exist, cannot find images.")

def create_output_folder(
    folder_path: str
) -> None:
    if os.path.exists(folder_path):
        outFolderRes = ""
        while outFolderRes not in ["y", "n", "yes", "no"]:
            outFolderRes = input(f"[{folder_path}] already exists. Continue adding images to to this folder? [y]es or [n]o?").lower()
            if outFolderRes in ["n", "no"]:
                print("Aborting...", end="")
                sys.exit()
    else:
        print(f"Creating output folder...", end="")
        os.makedirs(folder_path)
        print("done.")

# iterator for images
def grab_next_image(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file
