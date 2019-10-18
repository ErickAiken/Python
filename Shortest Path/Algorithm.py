#Genetic Algorithm
import numpy as np
import Utilities as Utils

###############################################
def Alg(Cities, population_size, generation_size, mutation_rate):
        
    #initialize
    nd_Cities = np.array(Cities)    
    Best_From_Each_Generation = []
    Best_Fit_From_Each_Generation = []
    
    for j in range(generation_size):
        
        Pop_list = []
        Fit_List = []
        
        for i in range(population_size):
            #scramble the cities
            temp = nd_Cities[np.random.choice(nd_Cities.shape[0], len(nd_Cities), replace = False)]
            #convert to list
            temp2 = np.ndarray.tolist(temp)
            #add to the population list
            Pop_list.append(temp2)
            #calculate the fitness
            Fit = Utils.Fitness(temp2)
            #Add to the Fit_List
            Fit_List.append(Fit)
        
        #find the best fit order and return it
        mini = Fit_List.index(min(Fit_List))
        Best = Pop_list[mini]
        
        #send out of loop
        Best_From_Each_Generation.append(Best)
        Best_Fit_From_Each_Generation.append(Fit_List[mini])
        
    #best of generations
    minum = Best_Fit_From_Each_Generation.index(min(Best_Fit_From_Each_Generation))
    Optimal_Path = Best_From_Each_Generation[minum]
    return Optimal_Path
    
###############################################




