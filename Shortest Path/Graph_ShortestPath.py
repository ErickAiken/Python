

import matplotlib.pyplot as plt
import Utilities as Utils

###############################################
def plotter(x_name, y_name, title, x_min, x_max, y_min, y_max, in_points, in_path, color):
    
    #convert the coordinates into X's and Y's
    points = Utils.CoordsToXY(in_points)
    path = Utils.CoordsToXY(in_path)
    
    #add the starting point to the end of the path array to close the loop
    path[0].append(path[0][0])
    path[1].append(path[1][0])
    
    #plot the cities
    plt.scatter(points[0],points[1], color = color)
    
    #connect the cities
    plt.plot(path[0],path[1], color = 'skyblue')
    
    #define the graph parameters
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.title(title)
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    
    #change the color of the first dot
    plt.plot(path[0][0], path[1][0], marker = 's', color = 'green')
    
    #create a list for the first two cities
    x_lis = [path[0][0], path[0][1]]
    y_lis = [path[1][0], path[1][1]]
    plt.plot(x_lis, y_lis, color = 'forestgreen')
    
    #finalize
    plt.show()
###############################################