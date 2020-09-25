import PIL.Image
import glob
import os

files = glob.glob("downloads/*.gif") 

for imageFile in files:
    filepath,filename = os.path.split(imageFile)
    filterame,exts = os.path.splitext(filename)
    print ("Processing: " + imageFile,filterame)
    im = PIL.Image.open(imageFile)
    im.save( 'downloads/'+filterame+'.png','PNG')