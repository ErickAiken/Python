#Read in the file and store as np.array()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#Create a pandas dataframe
dfTable = pd.read_csv('EmissionData.csv')

#Convert the dataframe to an ndArray
ndArr = np.asarray(dfTable)

#Store the names of countries
Names = ndArr[:,0]

#print(dfTable[['Country', '1751']])
world_1751 = 9350528
print("The world emissions in 1751: ", ndArr[227, 1])
worldemissions = ndArr[227,1:]

USA = ndArr[220,1:]
print(dfTable)
print(ndArr)
plt.plot(worldemissions)
plt.plot(USA)
plt.legend(('World', 'USA'), loc='upper left')
plt.title('Emissions')
plt.xlabel('Years since 1751')
plt.ylabel('Tonnes of CO2 and GHGs')
plt.show()