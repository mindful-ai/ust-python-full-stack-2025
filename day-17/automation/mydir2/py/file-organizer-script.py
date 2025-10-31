import os
import os.path
import shutil
import subprocess

path = r"."
os.chdir(r".")

files = os.listdir()

dirs = set([os.path.splitext(f)[1][1:] for f in files])

# Create the directories
for dir in dirs:
    os.mkdir(dir)

# Move the files
for file in files:
    src = file
    dest = os.path.splitext(file)[1][1:]
    finalDest = os.path.join(dest, file)
    shutil.move(src, finalDest)
    # print(finalDest)