# -*- coding: utf-8 -*-
"""
Created on Tue May 09 14:29:50 2017

@author: Libby
"""
import numpy as np
from scipy import ndimage
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import matplotlib.colors
import sys


class project_final(object):
    def __init__(self, name):
        self.name = name
    ##convert files to binary image files
    def biimage(object):
        plots = []
        for x in range(10):
            ##Allows user to indicate which color of water was used for experiment
            color = input("What color is the river? 1 = Blue, 2 = Red | Input: ")
            ##identify files
            filename = 'Img' + str(x+1) + ".jpg"
            ##define image
            im = mpimg.imread(filename)
            ##convert images to binary images
            hsv = matplotlib.colors.rgb_to_hsv(im)
            ##If river is blue, use this code
            if color == 1:
                river = hsv[:,:,0]-hsv[:,:,1] > -.5
                river = hsv[:,:,1] < .17
            ##If river is red, use this code
            elif color == 2:
                river = hsv[:,:,0]-hsv[:,:,1] < -.5
                river = hsv[:,:,1] > .55
            ##If color is not indicated, print error
            else:
                print("Error: Please choose color")
            ##Plot image     
            ##Allows user to indicate whether or not to print image
            imgplt = input("Plot image? 1 = Yes, 2 = No | Input: ")
            plt.imshow(river)
            #If yes, print image
            if imgplt == 1: 
                plt.show() 
            #If no, don't print image
            elif imgplt == 2:
                print("Ok, no plot, then.")
            #If yes or no not indicated, print error
            else:
                print("Error: Please indicate 'Yes' or 'No'")
            
    ##save images in folder
            plt.imsave("binary" + str(filename), river)
            
    ##save data in folder
            np.savetxt(str(filename) + ".txt", river, fmt = '%d')
        print("All images have been processed.")
    ##Exit system
        sys.exit()
        
newlist = project_final("Img1_Img10")
newlist.biimage()    
    
finalimg = project_final("Img1_Img10")
finalimg.biimage()




