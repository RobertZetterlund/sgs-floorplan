import glob 
import os

files = glob.glob("downloads/**.png")
print(files)

for file in files:
    filename = file.split(".")[0]
    os.rename(file, filename + ".gif")
