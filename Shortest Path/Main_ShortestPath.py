
#This algorithm will try to find the shortest path that visits each point
import Graph_ShortestPath as Graph
import Utilities as Utils
import Algorithm as Optimize

#define where the cities are
Cities = [[1,5],[2,4],[3,2],[4,3],[5,1], [8,9], [6,6], [4,8]]

#run the genetic algorithm
Optimal_Path = Optimize.Alg(Cities, 100, 100, 0)
print(Optimal_Path)

#fitness of the solution is 1/total_distance_traveled, closer to zero the better
Fitness = Utils.Fitness(Optimal_Path)

#graph the result
Graph.plotter("X-Axis", "Y-Axis","Optimal Path", 0, 10, 0, 10, Cities, Optimal_Path, "red")
print(Utils.Fitness(Optimal_Path))


