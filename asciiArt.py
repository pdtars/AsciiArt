# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 20:44:40 2019

@author: Paulo
"""
import argparse, sys, random
from PIL import Image
import numpy as np

# 70 levels of gray
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

# 10 levels of gray
gscale2 = "@%#*+=-:. "

#image = Image.open("FB_20150331_00_52_01_Saved_Picture.jpg").convert("L")

def getAverage(image):
    """
    Get PIL Image, return average value of greyscale value
    The reshape converts the two dimensional array (width and height) into
    a flat one-d array.
    """
    #Transform to numpy array , then get dimensions, finally avg
    im = np.array(image)
    w,h = im.shape
    return np.average(im.reshape(w*h))

def convertImageToAscii(fileName, cols, scale, moreLevels):
    """
    Given Image and dimensions (rows, cols), returns an 
    m*n list of Images
    """
    global gscale1, gscale2
    #Open Image and convert to greyscale
    image = Image.open(fileName).convert('L')
    #store the image dimensions
    W, H = image.size[0],image.size[1]
    print("input image dimensions: %d x %d" % (W,H))
    #Compute tile width
    w = W/cols
    #compute tile height based on the aspect ratio and scale of the font
    h = w/scale
    #compute number of rows to use in the final grid
    rows = int(H/h)
    
    print("cols: %d, rows: %d" % (cols,rows))
    print("tile dimensions: %d x %d" % (w,h))
    
    #check if image size is too small
    if cols > W or rows > H:
        print("Image is too small for specified cols!")
        #exit(0) means a clean exit without any errors / problems
        exit(0)
    
    # an ASCII image is a list of character strings
    aimg = []
    #generate the list of tile dimensions
    for j in range(rows):
        y1 = int(j*h)
        y2 = int((j+1)*h)
        #correct the last tile (up to but not included?)
        if j == rows-1:
            y2 = H
        # append an empty string
        aimg.append("")
        for i in range(cols):
            # crop the image to fit the tile
            x1 = int(w*i)
            x2 = int((i+1)*w)
            # corret the last tile
            if i == cols-1:
                x2 = W
            #crop the image to extract the file into another Image objct
            # LEFT , Right , Top , Bottom
            img = image.crop((x1, y1, x2, y2))
            avg = int(getAverage(img))
            # look up the ASCII char for grayscale value (avg)
            if moreLevels:
                gsval = gscale1[int((avg*69)/255)]
            else:
                gsval = gscale2[int((avg*9)/255)]
            # append the ascii character to the string
            aimg[j] += gsval
    #return text image
    return aimg


def main():
    # create parser
    descStr = "This program converts an image into ASCII art."
    #The ArgumentParser object will hold all the information necessary
    #to parse the command line into Python data types.
    parser = argparse.ArgumentParser(description=descStr)
    #add expected arguments
    parser.add_argument('--file', dest='imgFile', required=True)
    parser.add_argument('--scale', dest='scale', required=False)
    parser.add_argument('--out', dest='outFile', required=False)
    parser.add_argument('--cols', dest='cols', required=False)
    parser.add_argument('--morelevels', dest='moreLevels', action='store_true')
    
    #parse argumentos
    args = parser.parse_args()
    
    imgFile = args.imgFile
    #set output file
    outFile = 'out.txt'
    #If outfile was set...
    if args.outFile:
        outFile = args.outFile
    #set scale default as 0.43, suits a Courier font
    scale = 0.43
    if args.scale:
        scale = float(args.scale)
    #set cols
    cols = 80
    if args.cols:
        cols = int(args.cols)
    
    print('generating ASCII art...')
    #convert image to Ascii text
    aimg = convertImageToAscii(imgFile, cols, scale, args.moreLevels)
    
    #open a new text file
    f = open(outFile, 'w')
    #write each string in the list to the new file
    for row in aimg:
        f.write(row + '\n')
    # clean up
    f.close()
    print("ASCII art writtin to %s" % outFile)
    
# call main

if __name__ == '__main__':
    main()




