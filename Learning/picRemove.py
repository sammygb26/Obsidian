import os
import sys
import re
from tqdm import tqdm

def get_path():
    if len(sys.argv) <= 1:
        print(f"No path specified in argv, exiting.")
        quit()
    return sys.argv[1]

def get_subfolders(path : str):
    return [os.path.join(path, x) for x in os.listdir(path) if not "." in x]

def get_md_files(path : str):
    return [os.path.join(path, x) for x in os.listdir(path) if x.endswith(".md")]

def get_png_files(path : str):
    return [os.path.join(path, x) for x in os.listdir(path) if x.endswith(".png")]
    

def explore_path(path : str):
    subfolders = get_subfolders(path)
    mds = get_md_files(path)
    pngs = get_png_files(path)


    all_folders = subfolders
    all_md_files = mds
    all_png_files = pngs
    for folder in subfolders:
        sub, mds, pngs = explore_path(folder)

        all_folders += sub
        all_md_files += mds
        all_png_files += pngs


    return all_folders, all_md_files, all_png_files

def explore_file(filename : str):
    pictures : set[str] = set()

    try:
        file = open(filename, "r")
        lines = file.readlines()
        file.close()

        for line in lines:
            for pic in check_line(line):
                pictures.add(pic)
    except FileNotFoundError:
        print(f"{filename} not found!")

    return pictures

def check_line(line : str):
    return re.findall(r"(Pasted image \d{14}.png)+", line)


def main():
    path = get_path()

    _, mds, pngs = explore_path(path)
    
    pictures = set()
    for md in mds:
        pics = explore_file(md)
        pictures = pictures.union(pics)

    print(f"{len(pictures)} found.")
    
    unused = []

    for png in pngs:
        if check_line(png):
            if check_line(png)[0] in pictures:
                continue
        unused.append(png)

    print(f"{len(unused)} unused")

    for png in pngs[max(0, len(unused) - 10):len(unused)]:
        print(png)

    if input("Deleat(y)?:") == "y":
        for png in unused:
            os.remove(png)
        print("Done.")

if __name__ == "__main__":
    main()

