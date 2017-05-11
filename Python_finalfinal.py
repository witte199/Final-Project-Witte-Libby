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

class project_final(object):
    def __init__(self, name):
        self.name = name
    ##convert files to binary image files
    def biimage(object):
        plots = []
        for x in range(10):
            ##identify files
            filename = 'Img' + str(x+1) + ".jpg"
            ##define image
            im = mpimg.imread(filename)
            ##convert images to binary images
            hsv = matplotlib.colors.rgb_to_hsv(im)
            river = hsv[:,:,0]-hsv[:,:,1] > -.5
            river = hsv[:,:,1] < .17
            ##Plot image     
            plt.imshow(river)
            plt.show() 
            
    ##save data in folder
            plt.imsave("binary" + str(filename), river)
    
finalimg = project_final("Img1_Img10")
finalimg.biimage()

