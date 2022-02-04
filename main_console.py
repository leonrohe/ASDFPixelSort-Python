import os
import sys
import time
from PIL import Image
from pathlib import WindowsPath

#variables

threshold = 0

fileName = ""
img = None
pixels = None

width = 0
height = 0
start_time = 0

#functions

def brightness(color):  
    return max(color)

def findBrightness(c, offset):
    x = offset
    while(x<len(c)):
        if(brightness(c[x])<threshold):
            return x
        x = x + 1
    return len(c)

#main program

fileName = input("Input file name. (fileName.xyz)" + "\n")

#get file to use
try:
    img = Image.open(fileName)
    pixels = list(img.getdata())
    width = img.width
    height = img.height
except:
    print("Unable to open file." + "\n")
    os.system("pause")
    quit()

#get threshold to use
try:
    threshold = int(input("What threshold to use? (0-255)" + "\n"))
except:
    print("Unable to set threshold." + "\n")
    os.system("pause")
    quit()

#main 

start_time = time.time()

for y in range(0, height): 

    sys.stdout.write("\rProgress: " + str(y+1) + "/" + str(height))

    #get current pixel row
    row = pixels[y*width:y*width+width]

    #modify pixel row
    x = 0
    while(x<width):
        x1 = x
        x2 = findBrightness(row, x+1)

        r = x2-x1

        if(r>0):
            c_temp = row[x1:x1+r]

            c_temp = sorted(c_temp)

            i1 = y*width+x1
            i2 = y*width+x1+r

            pixels[i1:i2] = c_temp

        x = x2

#apply modified pixel row
img.putdata(pixels)

#get time it took for program to finish
print("\n"+"Processing finished in %s seconds." % (time.time() - start_time) + "\n")

#save image
saveString = os.path.splitext(img.filename)[0] + "_threshold_" + str(threshold) + ".png"
print("\n"+"File saved as " + saveString)
img.save(saveString)

#show image
img.show()

os.system("pause")
