#Lithium Atom - Main
import numpy as np
import Metropolis_LithiumAtom as Metropolis
import BuildAnim_LithiumAtom as BuildAnim
import matplotlib.pyplot as plt

#Ddefine variables
totalTime = 10000
delta = 4.9
Accepted = 0
r = np.empty((3, totalTime))

#Initialization
x = 1
y = 0
z = 0
r[0,0] = x
r[1,0] = y
r[2,0] = z
avgDistList = []
Distance = 0
avgSquares = 0
avgEmp = 0

#Motion
for time in range(1, totalTime):
    #Where am I?
    xOld = r[0, time-1]
    yOld = r[1, time-1]
    zOld = r[2, time-1]
    #Where do I want to go
    xTrial, yTrial, zTrial = Metropolis.TrialMove(xOld, yOld, zOld, delta)
    weight = Metropolis.MetroTest(xOld, yOld, zOld, xTrial, yTrial, zTrial)
    rTest = np.random.random()
    
    if(rTest < weight):
        #Accept
        r[0, time] = xTrial
        r[1, time] = yTrial
        r[2, time] = zTrial
        Distance = Distance + np.sqrt(r[0, time]**2 + r[1, time]**2 + r[2, time]**2)
        Accepted = Accepted + 1
        avgEmp = avgEmp + np.sqrt(r[0, time]**2 + r[1, time]**2 + r[2, time]**2)
        avgDistList.append(avgEmp/time)
        
    else:
        #Reject
        r[0, time] = xOld
        r[1, time] = yOld
        r[2, time] = zOld
        avgEmp = avgEmp + np.sqrt(r[0, time]**2 + r[1, time]**2 + r[2, time]**2)
        avgDistList.append(avgEmp/time)
        
#Plot the empirical average as a function of metropolis time
plt.plot(avgDistList)
plt.show()
BuildAnim.Animation3D(r)  
        
        
    
