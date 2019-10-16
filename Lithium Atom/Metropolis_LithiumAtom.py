#Lithium Atom - Metropolis
import numpy as np

#Random
def RandValue(x):
    return np.random.uniform(-x, x)

#Square Root
def SqRoot(x, y, z):
    return np.sqrt(x**2 + y**2 + z**2)

#Trial move
def TrialMove(x, y, z, delta):
    X = x + RandValue(delta)
    Y = y + RandValue(delta)
    Z = z + RandValue(delta)
    return X, Y, Z

#Metropolis test
def MetroTest(x, y, z, X, Y, Z):
    r = SqRoot(x, y, z)
    R = SqRoot(X, Y, Z)
    
    a = (2-R)**2
    b = (2-r)**2
    c = a/b
    
    return min(1.0, c*np.exp(-1*(R-r)))




    
