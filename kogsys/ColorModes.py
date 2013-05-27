#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://en.wikipedia.org/wiki/Hue#Computing_hue_from_RGB

import sys
from math import atan2, sqrt, acos, pi

# see http://fourier.eng.hmc.edu/e161/lectures/color_processing/node3.html
def RGBToHSI(R, G, B):
    # some needed values
    i = R + G + B
    r = R / i
    g = G / i
    b = B / i
    
    I = i / 3.0
    
    if (R==G and G == B):
        S = 0
        H = 0
    else:
        w = 0.5 * ((R - G + R - B) / sqrt((R - G) * (R - G) + (R - B) * (G - B )))
        if (w > 1):
            w = 1
        if (w < -1):
            w = -1
        
        H = acos(w)
        if (H < 0):
            print "H should not be negative"
        if (B > G):
            H = 2 * pi - H
        
        minimum = min(r, g, b)
        
        S = 1 - 3 * minimum
    return (H, S, I)
        


if __name__ == "__main__":
    # TODO: see http://stackoverflow.com/questions/642154/how-to-convert-strings-into-integers-in-python and try to "generate" the integer list
    
    # grab commandline arguments
    params = sys.argv[1:]
    
    # we need 3 parameters
    if (len(params) != 3):
        print "Please provide 3 arguments (RGB)"
    else:
        print "HSI (H in radiant): "+ str((RGBToHSI(int(params[0]), int(params[1]), int(params[2]))))
    
