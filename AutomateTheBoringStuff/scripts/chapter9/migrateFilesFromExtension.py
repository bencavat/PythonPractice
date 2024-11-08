#! python3

import os, shutil

sourceFolder = input("What's the source folder?") or "C:\\Users\\Ben Cavat\\PythonPractice\\AutomateTheBoringStuff\\scripts\\chapter9"
destinationFolder = input("What's the destination folder?") or "C:\\Users\\Ben Cavat\\PythonPractice\\AutomateTheBoringStuff\\scripts\\chapter9_copy"
targetExtension = input("What extension are we on the hunt for today?") or "jpg"

print(sourceFolder)
for folderName, subfolders, filenames in os.walk(sourceFolder):
    print(f"This is filenames: {filenames}")
    for file in filenames:
        print(f"checking for {file}")
        if targetExtension in file:
            # shutil.copy(file, destinationFolder)
            print(f"Copying {file} to {destinationFolder}")
