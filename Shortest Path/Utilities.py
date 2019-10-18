#utility functions
import numpy as np

###############################################
def CoordsToXY(in_array):
    
    x_coords = []
    y_coords = []
    
    #loop through the array
    for i in range(len(in_array)):
        x_coords.append(in_array[i][0])
        y_coords.append(in_array[i][1])
    
    #output
    out_array = [x_coords, y_coords]
    return out_array
###############################################
def Fitness(Path):
    
    #initialize the distance
    dist = 0
    
    #append the first point to complete the route
    final = [Path[0][0], Path[0][1]]
    Path.append(final)
    
    for i in range(len(Path)-1):
       #inital point
       x1 = Path[i][0]         
       y1 = Path[i][1]
       
       #final point
       x2 = Path[i+1][0]
       y2 = Path[i+1][1]
       
       #find the differences
       delta_x = abs(x2-x1)
       delta_y = abs(y2-y1)
       
       #calculate the hypotenuse
       r= np.sqrt(delta_x**2 + delta_y**2)
       
       dist = dist + r
       
    return 1/dist
###############################################
def replace(list, index, value):
    list.pop(index)
    list.insert(index, value)

        
###############################################

    
    