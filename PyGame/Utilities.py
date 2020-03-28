#collection of utility functions
import matplotlib as mpl


###################################################
def ColorString_to_RGB(color_string):
    
    RGB = mpl.colors.to_rgb(color_string)
    RGB = [i*255 for i in RGB]
    return RGB
    
###################################################


    
    
    