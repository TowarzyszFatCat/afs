import os
import shutil
import sys

# Variables
DIR = sys.argv[1]


def main():
    for root, subdirs, files in os.walk(DIR):
        for file in files:
            name, ext = os.path.splitext(file)
            fext = ext[1:]  # Get the file extension without the dot
            fpath = os.path.join(root, file)

            if fext != "":
                target_dir = os.path.join(DIR, fext)
                # Create directory if it doesn't exist
                os.makedirs(target_dir, exist_ok=True)
            else:
                target_dir = os.path.join(DIR, "_WExt_")
                # Create directory if it doesn't exist
                os.makedirs(target_dir, exist_ok=True)

            # Handle filename collisions
            target_file = os.path.join(target_dir, file)
            counter = 1

            while os.path.exists(target_file):
                target_file = os.path.join(target_dir, f"{name}_{counter}{ext}")
                counter += 1

            # Move the file to the target directory
            shutil.move(fpath, target_file)

    delete_empty_folders(DIR)


def delete_empty_folders(path):
    deleted = set()

    for current_dir, subdirs, files in os.walk(path, topdown=False):

        still_has_subdirs = False
        for subdir in subdirs:
            if os.path.join(current_dir, subdir) not in deleted:
                still_has_subdirs = True
                break

        if not any(files) and not still_has_subdirs:
            os.rmdir(current_dir)
            deleted.add(current_dir)

    return deleted


if __name__ == "__main__":
    try:
        main()
    except IndexError:
        print("You must specify path!")
